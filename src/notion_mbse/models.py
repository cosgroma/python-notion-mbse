#!/usr/bin/env python
"""
@package   models
Details:
Created:   Saturday, June 29th 2024, 7:16:19 pm
-----
Last Modified: 06/29/2024 08:13:33
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "models.py"
__version__ = "0.1.0"

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

# from pydantic.schema import schema
from bson import ObjectId
from databasetools.controller.base_controller import DatabaseController
from notion_objects import URL
from notion_objects import Checkbox
from notion_objects import Date
from notion_objects import MultiSelect
from notion_objects import Number
from notion_objects import Page
from notion_objects import Status
from notion_objects import Text
from notion_objects import TitleText
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

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

    model_config = ConfigDict(arbitrary_types_allowed=True, json_encoders={ObjectId: str})
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

    def set_with_element(self, element: "Element"):
        for key, value in element.model_dump().items():
            setattr(self, key, value)


class ControllableElement(Element):
    controller: Optional[DatabaseController] = Field(None, description="The controller that manages the element in the database.")

    def use_controller(self, controller: DatabaseController):
        self.controller = controller

    @classmethod
    def from_element(cls, element: Element):
        return cls(Element.model_dump())

    @classmethod
    def from_dict(cls, element_dict: Dict[str, Any]):
        return cls(**element_dict)

    def to_dict(self):
        return self.model_dump()

    def create(self):
        if self.controller:
            self.controller.create(self)
        else:
            raise ValueError("Element has no controller to create")

    def update(self):
        if self.controller:
            self.controller.update(self)
        else:
            raise ValueError("Element has no controller to update")

    def read(self):
        if self.controller:
            read_objs = self.controller.read(self)
            obj = read_objs[0]
            self.set_with_element(obj)
            # change the element attributes with the read object

        else:
            raise ValueError("Element has no controller to read")

    def __del__(self):
        if self.controller:
            self.controller.delete(self)


class BasePage(Page):
    name = TitleText("Name")

    def __str__(self):
        return f"{self.__class__.__name__}({self.id} - {self.name})"


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
