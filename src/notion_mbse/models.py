#!/usr/bin/env python
"""
@package   models
Details:
Created:   Saturday, June 29th 2024, 7:16:19 pm
-----
Last Modified: 06/30/2024 01:27:03
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "models.py"
__version__ = "0.1.0"

from datetime import datetime
from typing import Any
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional

# from pydantic.schema import schema
from bson import ObjectId
from notion_objects import URL
from notion_objects import Checkbox
from notion_objects import Date
from notion_objects import MultiSelect
from notion_objects import Number
from notion_objects import Page
from notion_objects import Status
from notion_objects import Text
from notion_objects import TitleText
from notion_objects.properties import Property
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import field_serializer

from .base_controller import BaseController


class PydanticObjectId(ObjectId):
    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        if isinstance(v, str) and ObjectId.is_valid(v):
            return str(ObjectId(v))
        raise ValueError("Invalid ObjectId")

    @classmethod
    def __get_pydantic_json_schema__(cls, model_config, handler):
        return {"type": "string", "format": "ObjectId"}


class Element(BaseModel):
    """A base element contains common attributes that are shared by all elements. It contains information about the unique identifier, name, description, version, tags, type, sub-type, created by, created at, modified by, modified at, status, and documentation."""

    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: PydanticObjectId = Field(
        default_factory=PydanticObjectId,
        description="The unique identifier of the element.",
    )
    name: Optional[str] = Field(None, description="The name of the element.")
    description: Optional[str] = Field(None, description="The description of the element.")
    version: Optional[str] = Field(None, description="The version of the element.")
    tags: List[str] = Field([], description="The tags associated with the element.")
    type: Optional[str] = Field(None, description="The type of the element.")
    sub_type: Optional[str] = Field(None, description="The sub-type of the element.")
    created_by: Optional[str] = Field(None, description="The user who created the element.")
    created_at: datetime = Field(
        default_factory=datetime.now,
        description="The date and time the element was created.",
    )
    modified_by: Optional[str] = Field(None, description="The user who last modified the element.")
    modified_at: Optional[datetime] = Field(None, description="The date and time the element was last modified.")
    status: Optional[str] = Field(None, description="The status of the element.")
    documentation: Optional[str] = Field(None, description="The documentation associated with the element.")
    ref_ids: List[str] = Field([], description="The reference IDs associated with the element.")

    @field_serializer("modified_at")
    def serialize_dt(self, modified_at: datetime, _info):
        if modified_at is None:
            return None
        return modified_at.timestamp()

    # @field_serializer("id")
    # def serialize_id(self, id: PydanticObjectId, _info):
    #     return str(id)

    # @model_serializer
    # def ser_model(self) -> Dict[str, Any]:
    #     return {
    #         "id": str(self.id),
    #         "name": self.name,
    #         "description": self.description,
    #         "version": self.version,
    #         "tags": self.tags,
    #         "type": self.type,
    #         "sub_type": self.sub_type,
    #         "created_by": self.created_by,
    #         "created_at": self.created_at,
    #         "modified_by": self.modified_by,
    #         "modified_at": self.modified_at,
    #         "status": self.status,
    #         "documentation": self.documentation,
    #         "ref_ids": self.ref_ids
    #     }

    def set_with_element(self, element: "Element"):
        for key, value in element.model_dump().items():
            setattr(self, key, value)


class ControllableElement(Element):
    controller: Optional[BaseController] = Field(None, description="The controller that manages the element in the database.")

    def use_controller(self, controller: BaseController):
        self.controller = controller

    def to_element(self) -> Element:
        return Element(**self.model_dump())

    @classmethod
    def from_element(cls, element: Element):
        return cls(**element.model_dump())

    @classmethod
    def from_dict(cls, element_dict: Dict[str, Any]):
        return cls(**element_dict)

    def to_dict(self):
        return self.model_dump()

    def create(self):
        if self.controller is not None:
            obj = self.controller.create(self.to_element())
            self.set_with_element(obj)
        else:
            raise ValueError("Element has no controller to create")

    def update(self):
        if self.controller is not None:
            self.controller.update(self.to_element())
        else:
            raise ValueError("Element has no controller to update")

    def read(self):
        if self.controller is not None:
            read_objs = self.controller.read(self.to_element())
            obj = read_objs[0]
            self.set_with_element(obj)
            # change the element attributes with the read object

        else:
            raise ValueError("Element has no controller to read")

    def delete(self):
        if self.controller is not None:
            self.controller.delete(self)


class BasePage(Page):
    name = TitleText("Name")

    def __str__(self):
        return f"{self.__class__.__name__}({self.id} - {self.name})"

    def get_properties(self) -> Iterable[Property]:
        return super()._get_properties()


def create_dynamic_page_class(name, fields):
    return type(name, (BasePage,), fields)


SCHEMA_TO_NOTION_TYPE = {
    "string": Text,
    "array": MultiSelect,
    "number": Number,
    "boolean": Checkbox,
    "date-time": Date,
    "ObjectId": Text,
}

SPECIAL_FIELDS = {
    "name": TitleText("Name"),
    "status": Status("Status"),
    "link": URL("URL"),
    "website": URL("Website"),
    "email": URL("Email"),
    "phone": URL("Phone"),
    "tags": MultiSelect("Tags"),
}


def create_db_page_from_schema(schema):
    if schema["type"] != "object":
        raise ValueError("Schema must be an object")

    if "title" not in schema:
        raise ValueError("Schema must have a title")

    if "properties" not in schema:
        raise ValueError("Schema must have properties")

    if not schema["properties"] or len(schema["properties"]) == 0:
        raise ValueError("Schema must have properties")

    name = f"Notion{schema['title']}"

    fields = {}

    for field, field_schema in schema["properties"].items():
        if "anyOf" in field_schema:
            non_null_field = next([afield["type"] for afield in field_schema["anyOf"] if afield["type"] != "null"])
        else:
            non_null_field = field_schema["type"]

        if field in SPECIAL_FIELDS:
            fields[field] = SPECIAL_FIELDS[field]
        elif non_null_field in SCHEMA_TO_NOTION_TYPE:
            fields[field] = SCHEMA_TO_NOTION_TYPE[non_null_field](field_schema["title"])
        else:
            fields[field] = Text(field_schema["title"])
    return type(name, (BasePage,), fields)
