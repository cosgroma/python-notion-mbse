# from pymongo import MongoClient
import os
from typing import List

import dotenv
from databasetools import NotionPage
from databasetools.adapters.notion import utils

# from pydantic.schema import schema
from notion_objects import Property

from notion_mbse.models import Element
from notion_mbse.models import create_db_page_from_schema

dotenv.load_dotenv()


NOTION_API_KEY = os.getenv("NOTION_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
NOTION_OMG_SPEC_DB_URL = os.getenv("NOTION_OMG_SPEC_DB_URL")
NOTION_MBSE_ROOT_URL = os.getenv("NOTION_MBSE_ROOT_URL")

## Data Models


def test_schema_to_notion():
    element_schema = Element.model_json_schema()
    NotionElement = create_db_page_from_schema(element_schema)
    assert NotionElement.name.field == "Name"
    assert NotionElement.description.field == "Description"
    assert NotionElement.version.field == "Version"

    # properties: List[Property] = NotionElement.get_properties()
    # for prop in properties:
    #     print(prop.field, prop.type, prop.attr, type(prop.attr))

    # page = NotionElement.new(name="Test", description="", version="", status="Done", tags=["tag1", "tag2"])

    # pprint(page.to_json())


# NotionPage Methods:
# * `def set_local_dir(self, local_dir: Union[str, Path])`
# * `def get_file_path(self) -> Path`
# * `def set_file_path(self, file_name: Union[str, Path])`
# * `def save(self, type: str = "json", recursive: bool = False, file_name: Optional[str] = None, parent_name: Optional[str] = None) -> Path`
# * `def get_page(self, force: bool = False) -> Tuple[Page, dict]`
# * `def get_blocks(self, force: bool = False) -> List[dict]`
# * `def set_blocks(self, blocks: List[dict], clear: bool = False)`
# * `def clear_blocks(self)`
# * `def add_page(self, title: str) -> "NotionPage"`
# * `def add_database(self, title: str) -> "NotionDatabase"`
# * `def get_children(self, force: bool = False, recursive: bool = False) -> List[Union["NotionPage", "NotionDatabase"]]`
# * `def get_child_pages(self, force: bool = False) -> List["NotionPage"]`
# * `def get_child_databases(self, force: bool = False) -> List["NotionDatabase"]`


def test_get_notion_page():
    mbse_root_page_id = utils.extract_id_from_notion_url(NOTION_MBSE_ROOT_URL)
    mbse_root_page = NotionPage(token=NOTION_API_KEY, page_id=mbse_root_page_id, load=True)
    # Add a profiles page to the root page
    # Get child pages
    child_pages = mbse_root_page.get_child_pages()
    blocks = mbse_root_page.get_blocks()
    print("Blocks:")
    for block in blocks:
        if block["type"] == "child_database":
            print(block)
    has_profiles = False
    for page in child_pages:
        if page.title == "Profiles":
            has_profiles = True
            print("Profiles page found")
            profiles_page = page
            break
    if not has_profiles:
        profiles_page = mbse_root_page.add_page("Profiles")
        print(profiles_page.title)

    # Get child databases of the mbse root page
    # mbse_databases = mbse_root_page.get_child_databases(force=True)

    has_elements_db = False
    # if len(mbse_databases) == 0:
    #     print("No databases found")
    # else:
    #     for db in mbse_databases:
    #         print(utils.get_title_content(db.title))
    #         if utils.get_title_content(db.title) == "Elements":
    #             has_elements_db = True
    #             print("Elements database found")
    #             elements_db = db
    #             break
    if not has_elements_db:
        print("Creating Elements database")
        elements_db = mbse_root_page.add_database("Elements")

    # NotionDatabase Methods:
    # * `def set_parent(self, parent: NotionPage)`
    # * `def set_parent_by_id(self, parent_id: str)`
    # * `def get_parent(self) -> NotionPage`
    # * `def get_parent_id(self) -> str`
    # * `def get_property_map(self, source_properties: List[str], threshold: int = 80) -> Dict[str, str]`
    # * `def get_properties(self) -> Dict[str, Any]`
    # * `def add_property(self, prop_name: str, prop_type: Optional[str] = "rich_text", prop_info: Optional[Dict[str, Any]] = None)`
    # * `def remove_property(self, prop_name: str)`
    # * `def get_children(self, force: bool = False) -> List[NotionPage]`
    # * `def get_pages(self, force: bool = False) -> List[NotionPage]`
    # * `def check_if_exists(self, title: str) -> bool`
    # * `def create(self, properties: Optional[Dict[str, Any]] = None, obj: Optional[NotionObject] = None) -> NotionObject`
    # * `def read(self, entry_id: str) -> NotionObject`
    # * `def update(self, entry: NotionObject, properties: Optional[Dict[str, Any]] = None) -> NotionObject`
    # * `def delete(self, entry: NotionObject)`
    # * `def delete_all(self)`
    # * `def query(self, filter: Optional[dict] = None) -> List[NotionObject]`

    db_properties = elements_db.get_properties()
    print("Database properties before:")
    for prop in db_properties:
        print(prop, db_properties[prop])

    # make this an elements database by adding the element schema
    element_schema = Element.model_json_schema()
    NotionElement = create_db_page_from_schema(element_schema)

    properties: List[Property] = NotionElement.get_properties()

    for prop in properties:
        print(prop.field, prop.type, prop.attr)
        prop_name = prop.field
        prop_type = prop.type
        # prop_info = {}
        if prop_name not in db_properties:
            if prop_type is None:
                print(f"Property {prop_name} has no type, skipping.")
                continue
            print(f"Adding property {prop_name} to database with type {prop_type}")
            elements_db.add_property(prop_name, prop_type, None)

    db_properties = elements_db.get_properties()
    print("Database properties after:")
    for prop in db_properties:
        print(prop, db_properties[prop])


# created_time None created_time
# last_edited_time None last_edited_time
# Name title name
# Ref Ids multi_select ref_ids
# Status status status
# Tags multi_select tags

# Created By rich_text created_by
# Description rich_text description
# Documentation rich_text documentation
# Id rich_text id
# Modified At rich_text modified_at
# Modified By rich_text modified_by
# Sub Type rich_text sub_type
# Type rich_text type
# Version rich_text version
