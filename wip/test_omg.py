from typing import Dict, Any, List, Optional
import requests
from bs4 import BeautifulSoup

# from pymongo import MongoClient
from pydantic import BaseModel, Field

import os
from pprint import pprint
import json
import logging
import os
from datetime import datetime
from pathlib import Path

from bson import ObjectId
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

# from pydantic.schema import schema

import pytz

from notion_objects import Checkbox
from notion_objects import Date
from notion_objects import MultiSelect
from notion_objects import Number
from notion_objects import Page
from notion_objects import Status
from notion_objects import Text
from notion_objects import TitleText
from notion_objects import URL

from databasetools import NotionBlock
from databasetools import NotionClient
from databasetools import NotionDatabase
from databasetools import NotionPage
from databasetools.adapters.notion import utils

import dotenv

dotenv.load_dotenv()


NOTION_API_KEY = os.getenv("NOTION_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
NOTION_OMG_SPEC_DB_URL = os.getenv("NOTION_OMG_SPEC_DB_URL")

## Data Models

### Basic Specification


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

    model_config = ConfigDict(
        arbitrary_types_allowed=True, json_encoders={ObjectId: str}
    )
    id: PydanticObjectId = Field(
        default_factory=PydanticObjectId,
        description="The unique identifier of the element.",
    )
    name: Optional[str] = Field(None, description="The name of the element.")
    description: Optional[str] = Field(
        None, description="The description of the element."
    )
    version: Optional[str] = Field(None, description="The version of the element.")
    tags: List[str] = Field([], description="The tags associated with the element.")
    type: Optional[str] = Field(None, description="The type of the element.")
    sub_type: Optional[str] = Field(None, description="The sub-type of the element.")
    created_by: Optional[str] = Field(
        None, description="The user who created the element."
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        description="The date and time the element was created.",
    )
    modified_by: Optional[str] = Field(
        None, description="The user who last modified the element."
    )
    modified_at: Optional[datetime] = Field(
        None, description="The date and time the element was last modified."
    )
    status: Optional[str] = Field(None, description="The status of the element.")
    documentation: Optional[str] = Field(
        None, description="The documentation associated with the element."
    )


from notion_objects import Checkbox
from notion_objects import Date
from notion_objects import MultiSelect
from notion_objects import Number
from notion_objects import Page
from notion_objects import Status
from notion_objects import Text
from notion_objects import TitleText
from notion_objects import URL

from databasetools import NotionBlock
from databasetools import NotionClient
from databasetools import NotionDatabase
from databasetools import NotionPage
from databasetools.adapters.notion import utils


# notion_update_specifications(NOTION_OMG_SPEC_DB_URL)


class BasePage(Page):
    name = TitleText("Name")

    def __str__(self):
        return f"{self.__class__.__name__}({self.id} - {self.name})"


def create_dynamic_page_class(name, fields):
    return type(name, (BasePage,), fields)


element_schema_orig = {
    "description": "A base element\n"
    "\n"
    "A base element contains common attributes that are shared by "
    "all elements. It contains information about the unique "
    "identifier, name, description, version, tags, type, sub-type, "
    "created by, created at, modified by, modified at, status, and "
    "documentation.",
    "properties": {
        "created_at": {
            "description": "The date and time the element " "was created.",
            "format": "date-time",
            "title": "Created At",
            "type": "string",
        },
        "created_by": {
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "default": None,
            "description": "The user who created the " "element.",
            "title": "Created By",
        },
        "description": {
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "default": None,
            "description": "The description of the " "element.",
            "title": "Description",
        },
        "documentation": {
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "default": None,
            "description": "The documentation associated " "with the element.",
            "title": "Documentation",
        },
        "id": {
            "description": "The unique identifier of the element.",
            "format": "ObjectId",
            "title": "Id",
            "type": "string",
        },
        "modified_at": {
            "anyOf": [{"format": "date-time", "type": "string"}, {"type": "null"}],
            "default": None,
            "description": "The date and time the element " "was last modified.",
            "title": "Modified At",
        },
        "modified_by": {
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "default": None,
            "description": "The user who last modified the " "element.",
            "title": "Modified By",
        },
        "name": {
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "default": None,
            "description": "The name of the element.",
            "title": "Name",
        },
        "status": {
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "default": None,
            "description": "The status of the element.",
            "title": "Status",
        },
        "sub_type": {
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "default": None,
            "description": "The sub-type of the element.",
            "title": "Sub Type",
        },
        "tags": {
            "default": [],
            "description": "The tags associated with the element.",
            "items": {"type": "string"},
            "title": "Tags",
            "type": "array",
        },
        "type": {
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "default": None,
            "description": "The type of the element.",
            "title": "Type",
        },
        "version": {
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "default": None,
            "description": "The version of the element.",
            "title": "Version",
        },
    },
    "title": "Element",
    "type": "object",
}

SCHEMA_TO_NOTION_TYPE = {
    "string": Text,
    "array": MultiSelect,
    "number": Number,
    "boolean": Checkbox,
    "date-time": Date,
    "ObjectId": Text,
}

SPECIAL_FIELDS = {
    "status": Status("Status"),
    "link": URL("URL"),
    "website": URL("Website"),
    "email": URL("Email"),
    "phone": URL("Phone"),
    "tags": MultiSelect("Tags"),
}

def create_dynamic_page_class_from_schema(schema):
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
            non_null_field = [afield["type"] for afield in field_schema["anyOf"] if afield["type"] != "null"][0]
        else:
            non_null_field = field_schema["type"]

        if field in SPECIAL_FIELDS:
            fields[field] = SPECIAL_FIELDS[field]
        elif non_null_field in SCHEMA_TO_NOTION_TYPE:
            fields[field] = SCHEMA_TO_NOTION_TYPE[non_null_field](field_schema["title"])
        else:
            fields[field] = Text(field_schema["title"])
    return type(name, (BasePage,), fields)

def test_create_dynamic_page_class():
    fields = {
        "description": Text("Description"),
        "version": Text("Version"),
    }
    DynamicPage = create_dynamic_page_class("DynamicPage", fields)
    print(type(DynamicPage))

    assert DynamicPage.name.field == "Name"
    assert DynamicPage.description.field == "Description"
    assert DynamicPage.version.field == "Version"

    page = DynamicPage.new(name="Test", description="", version="")
    assert page.name == "Test"
    assert page.description == ""
    print(page)


# test_create_dynamic_page_class()

def test_schema_to_notion():
    element_schema = Element.model_json_schema()
    # print(element_schema)
    DynamicElement = create_dynamic_page_class_from_schema(element_schema)
    assert DynamicElement.name.field == "Name"
    assert DynamicElement.description.field == "Description"
    assert DynamicElement.version.field == "Version"
    
    page = DynamicElement.new(name="Test", description="", version="", status="Done", tags=["tag1", "tag2"])
    
    pprint(page.to_json())
    
test_schema_to_notion()