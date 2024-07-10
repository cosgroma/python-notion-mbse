import os
import re
from pprint import pprint
from typing import Any
from typing import Dict
from typing import List

from notion_client import Client
from notion_objects import URL
from notion_objects import Checkbox
from notion_objects import MultiSelect
from notion_objects import NotionObject
from notion_objects import Number

# from pydantic.schema import schema
from notion_objects import Select
from notion_objects import TitleText

from notion_mbse.models.notion import BasePage
from notion_mbse.models.notion import create_db_page_from_schema

NOTION_API_KEY = os.getenv("NOTION_API_KEY", None)


def test_notion_client():
    client = Client(auth=NOTION_API_KEY)
    assert client
    # Test search recent pages
    payload = {
        "filter": {
            "value": "page",
            "property": "object",
        },
        "sort": {
            "direction": "descending",
            "timestamp": "last_edited_time",
        },
        "page_size": 10,
    }
    results: List[Dict[str, Any]] = client.search(**payload).get("results")
    assert results
    for result in results:
        pprint(result)
        page = NotionObject.new(**result)
        print(page.id, page.created_time, page.last_edited_time)
        break

    # database: Database[Page] = Database(Page, database_id="123456789abcdef1234567890abcdef1", client=notion)

    # result = database.query({
    #     "filter": {
    #         "timestamp": "last_edited_time",
    #         "last_edited_time": {
    #             "after": "2022-10-08"
    #         }
    #     }
    # })
    # for page in result:
    #     print(page.id, page.created_time, page.last_edited_time)
    # # Test search recent blocks
    # payload = {
    #     "filter": {
    #         "value": "block",
    #         "property": "object",
    #     },
    #     "sort": {
    #         "direction": "descending",
    #         "timestamp": "last_edited_time",
    #     },

    # }
    # results = client.search(**payload).get("results")
    # for result in results:
    #     pprint(result)
    #     break


def test_create_db_page_from_schema():
    schema = {
        "type": "object",
        "title": "TestSchema",
        "properties": {
            "name": {"type": "string", "title": "Name"},
            "age": {"type": "number", "title": "Age"},
            "is_active": {"type": "boolean", "title": "Is Active"},
            "tags": {"type": "array", "title": "Tags"},
        },
    }

    PageClass = create_db_page_from_schema(schema)

    assert issubclass(PageClass, BasePage)
    assert isinstance(PageClass.name, TitleText)
    assert isinstance(PageClass.age, Number)
    assert isinstance(PageClass.is_active, Checkbox)
    assert isinstance(PageClass.tags, MultiSelect)

    # test get
    assert PageClass.get("name") == PageClass.name
    assert PageClass.get("age") == PageClass.age
    assert PageClass.get("is_active") == PageClass.is_active
    assert PageClass.get("tags") == PageClass.tags


# def test_bad_schema():
#     schema = {
#         "type": "object",
#         "title": "TestSchema",
#         "properties": {
#             "name": {"type": "string", "title": "Name"},
#             "age": {"type": "number", "title": "Age"},
#             "is_active": {"type": "boolean", "title": "Is Active"},
#             "tags": {"type": "array", "title": "Tags"},
#         },
#     }

#     # remove the title from the schema
#     del schema["title"]

#     try:
#         PageClass = create_db_page_from_schema(schema)
#     except ValueError as e:


def test_create_db_page_from_schema_with_special_fields():
    schema = {
        "type": "object",
        "title": "TestSchema",
        "properties": {
            "name": {"type": "string", "title": "Name"},
            "status": {"type": "string", "title": "Status"},
            "link": {"type": "string", "title": "URL"},
            "website": {"type": "string", "title": "Website"},
            "email": {"type": "string", "title": "Email"},
            "phone": {"type": "string", "title": "Phone"},
            "tags": {"type": "array", "title": "Tags"},
        },
    }

    PageClass = create_db_page_from_schema(schema)

    assert issubclass(PageClass, BasePage)
    assert isinstance(PageClass.name, TitleText)
    assert isinstance(PageClass.status, Select)
    assert isinstance(PageClass.link, URL)
    assert isinstance(PageClass.website, URL)
    assert isinstance(PageClass.email, URL)
    assert isinstance(PageClass.phone, URL)
    assert isinstance(PageClass.tags, MultiSelect)


REGEX_PATTERNS = {
    # any field that starts with _
    "relation": r"^_.+$",
}


def check_field_for_regex(field: str) -> bool:
    for pattern in REGEX_PATTERNS.values():
        if re.match(pattern, field):
            return True
    return False


def test_check_field_for_regex():
    assert check_field_for_regex("_relation")
    assert not check_field_for_regex("relation")
    assert check_field_for_regex("_field")
    assert not check_field_for_regex("field")
