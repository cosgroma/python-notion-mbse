#!/usr/bin/env python
"""
@package   models
Details:
Created:   Saturday, June 29th 2024, 7:16:19 pm
-----
Last Modified: 07/09/2024 02:42:37
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "notion.py"
__version__ = "0.1.0"

import logging
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import Union

# from pydantic.schema import schema
from notion_objects import URL
from notion_objects import Checkbox
from notion_objects import Date
from notion_objects import MultiSelect
from notion_objects import Number
from notion_objects import Page
from notion_objects import Relation
from notion_objects import Select
from notion_objects import Text
from notion_objects import TitleText
from notion_objects.properties import Property

notion_logger = logging.getLogger(__name__)


class BasePage(Page):
    name = TitleText("Name")

    def __str__(self):
        return f"{self.__class__.__name__}({self.id} - {self.name})"

    @classmethod
    def get(cls, field: str) -> Any:
        return getattr(cls, field, None)

    @classmethod
    def get_properties(cls) -> List[Property]:
        return [field for field in cls.__properties__ if isinstance(field, Property)]


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
    "status": Select("Status"),
    "link": URL("URL"),
    "website": URL("Website"),
    "email": URL("Email"),
    "phone": URL("Phone"),
    "tags": MultiSelect("Tags"),
    "type": Select("Type"),
    "sub_type": Select("Sub-Type"),
}

SKIP_FIELDS = {
    "id": Text("ID"),
    "created_at": Date("Created At"),
    "modified_at": Date("Modified At"),
    "created_by": Text("Created By"),
    "modified_by": Text("Modified By"),
    "documentation": Text("Documentation"),
    "ref_ids": Relation("Ref IDs"),
}


def create_db_page_from_schema(schema: Dict[str, Union[str, Dict[str, Any]]]) -> Type[BasePage]:
    """
    Create a database page class dynamically based on the given schema.

    Args:
        schema (Dict[str, Union[str, Dict[str, Any]]]): The schema defining the structure of the database page.

    Returns:
        Type[BasePage]: The dynamically created database page class.

    Raises:
        ValueError: If the schema is not an object, does not have a title, does not have properties, or has no properties.

    """
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
            non_null_field_list = [afield["type"] for afield in field_schema["anyOf"] if afield["type"] != "null"]
            non_null_field = non_null_field_list[0] if len(non_null_field_list) == 1 else "string"
        else:
            non_null_field = field_schema["type"]

        if field.lower() in SKIP_FIELDS:
            notion_logger.info(f"Skipping field {field}")
            continue
        elif field in SPECIAL_FIELDS:
            special_field = SPECIAL_FIELDS[field]
            notion_logger.info(f"Adding special field {field} with type {special_field}")
            fields[field] = special_field
        elif non_null_field in SCHEMA_TO_NOTION_TYPE:
            fields[field] = SCHEMA_TO_NOTION_TYPE[non_null_field](field_schema["title"])
        else:
            notion_logger.info(f"Adding basic text field {field} with title {field_schema['title']}")
            fields[field] = Text(field_schema["title"])

    return type(name, (BasePage,), fields)


# class NotionEnhancedPage(NotionPage):
#     def add_database_with_model(self, title: str, model: BaseModel):
#         """Add a database to the current page."""
#         database = self.n_client.client.databases.create(
#             parent={"page_id": self.page_id}, title=[{"text": {"content": title}}], properties={"Name": {"title": {}}}
#         )
#         return NotionDatabase(token=self.n_client.token, database_id=database["id"])
