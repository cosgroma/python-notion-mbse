#!/usr/bin/env python
"""
@package   notion_database
Details:
Created:   Saturday, July 6th 2024, 3:35:06 pm
-----
Last Modified: 07/09/2024 04:24:06
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "notion_database.py"
__version__ = "0.1.0"

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from fuzzywuzzy import fuzz
from notion_objects import Database
from notion_objects import NotionObject
from notion_objects import Page

# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.DiGraph()
from .notion_base import BaseNotionDatabase
from .notion_base import BaseNotionPage
from .notion_client_extend import NotionClient
from .notion_utils import logger

NOTION_API_KEY = os.getenv("NOTION_API_KEY", None)

DATABASE_PROPERTIES = {
    "number": {},
    "formula": {},
    "select": {},
    "multi_select": {},
    "status": {},
    "relation": {},
    "rollup": {},
    "unique_id": {},
    "title": {},
    "rich_text": {},
    "url": {},
    "people": {},
    "files": {},
    "email": {},
    "phone_number": {},
    "date": {},
    "checkbox": {},
    "created_by": {},
    "created_time": {},
    "last_edited_by": {},
    "last_edited_time": {},
    "button": {},
    "location": {},
    "verification": {},
    "last_visited_time": {},
    "name": {},
}

# "parent": {
# "type": "page_id",
# "page_id": "7f64948c-b0c0-46e4-95c4-fb7e93813488"
# },
# "parent": {
# "type": "workspace",
# "workspace": true
# },
# "parent": {
# "type": "block_id",
# "block_id": "1c8561b8-1d2e-41f5-b11c-f9f0d5096b16"
# },


class NotionDatabase(BaseNotionDatabase):
    """Notion Database Class

    Attributes:

        token (str): The authentication token for accessing the Notion API.
        database_id (str): The ID of the Notion database.
        DataClass (Optional[NotionObject]): The custom data class for database entries.
        n_client (NotionClient): The Notion client object.
        database (Database): The Notion database object.
        properties (Dict[str, Any]): The properties of the database.
        pages (List[BaseNotionPage]): The list of pages in the database.
        parent (Optional[BaseNotionPage]): The parent page of the database.
        custom_data_class (bool): Flag to indicate if a custom data class is used.

    Methods:

        set_parent(parent: BaseNotionPage): Set the parent page of the database.
        set_parent_by_id(parent_id: str): Set the parent page by ID.
        get_parent() -> BaseNotionPage: Get the parent page.
        get_parent_id() -> str: Get the parent page ID.
        get_property_map(source_properties: List[str], threshold: int = 80) -> Dict[str, str]: Get the property mappings.
        load_from_json(json_path: Union[str, Path], database_id: str, DataClass: Optional[NotionObject] = None, create_properties: bool = False, force: bool = False): Load data from JSON file.
        load_database(database_id: str): Load the database.
        get_properties() -> Dict[str, Any]: Get the database properties.
        add_property(prop_name: str, prop_type: Optional[str] = "rich_text", prop_info: Optional[Dict[str, Any]] = None): Add a property to the database.
        remove_property(prop_name: str): Remove a property from the database.
        get_children(force: bool = False) -> List[BaseNotionPage]: Get the children of the database.
        get_pages(force: bool = False) -> List[BaseNotionPage]: Get the pages in the database.
        create(properties: Optional[Dict[str, Any]] = None, obj: Optional[NotionObject] = None) -> NotionObject: Create a database entry.
        check_if_exists(title: str) -> bool: Check if a database entry exists.

    Example Usage:

        ```python
        database = NotionDatabase(token="your-integration-token", database_id="your-database-id")
        database.load_database(database_id="your-database-id")
        database.get_properties()
        database.add_property("Name", "rich_text")
        database.remove_property("Name")
        database.get_children()
        database.get_pages()
        database.create({"Name": "John Doe"})
        database.check_if_exists("John Doe")
        ```
    """

    def __init__(self, token: Optional[str] = None, database_id: Optional[str] = None, DataClass: Optional[NotionObject] = None):
        if NOTION_API_KEY:
            token = NOTION_API_KEY
        if token is None:
            raise ValueError("No token provided.")
        self.token = token
        self.n_client = NotionClient(token=token)
        self.database_id = database_id

        if DataClass is None:
            self.DataClass = Page
            self.custom_data_class = False
        else:
            self.custom_data_class = True
            self.DataClass = DataClass

        if not issubclass(self.DataClass, NotionObject):
            raise ValueError("DataClass must be a subclass of NotionObject.")

        self.database: Optional[Database[self.DataClass]] = None
        self.properties: Dict[str, Any] = {}
        self.pages: List[BaseNotionPage] = []
        self.parent: Optional[BaseNotionPage] = None

        if self.database_id is not None:
            self.load_database(database_id)

    def set_parent(self, parent: BaseNotionPage):
        self.parent = parent

    def set_parent_by_id(self, parent_id: str):
        self.parent = BaseNotionPage(token=self.token, page_id=parent_id, load=False)

    def get_parent(self) -> BaseNotionPage:
        return self.parent

    def get_parent_id(self) -> str:
        return self.parent.page_id

    def get_property_map(self, source_properties: List[str], threshold: int = 80) -> Dict[str, str]:
        mappings = {}
        db_prop_names = [prop["name"] for prop in self.get_properties().values()]

        for src_property in source_properties:
            best_match = None
            best_score = 0
            for prop in db_prop_names:
                score = fuzz.ratio(src_property.lower(), prop.lower())
                if score > best_score:
                    best_score = score
                    best_match = prop
            if best_score > threshold:  # Threshold for fuzzy match
                mappings[src_property] = best_match
                db_prop_names.remove(best_match)

        return mappings

    def load_from_json(
        self,
        json_path: Union[str, Path],
        database_id: str,
        DataClass: Optional[NotionObject] = None,
        create_properties: bool = False,
        force: bool = False,
    ):
        self.database_id = database_id
        self.DataClass = DataClass
        self.load_database(database_id)

        with Path.open(json_path) as f:
            records: List[Dict[str, Any]] = json.load(f)

        # filename = Path(json_path).stem
        # print(filename)
        record = records[0]
        properties = record.keys()
        # generate_model_class_code(filename, properties, file_path=None)

        db_prop_names = [prop["name"].lower() for prop in self.get_properties().values()]
        print(f"Database properties: {db_prop_names}")
        properties_map = self.get_property_map(properties, threshold=80)
        print(f"Property mappings: {properties_map}")
        for prop in properties:
            if prop in properties_map and properties_map[prop] in db_prop_names:
                print(f"Mapping '{prop}' to '{properties_map[prop]}'")
                continue
            else:
                logger.warning(f"Property '{prop}' not found in database properties.")
                if create_properties:
                    prop_type = "rich_text"
                    if isinstance(record[prop], str):
                        prop_type = "rich_text"
                    elif isinstance(record[prop], int):
                        prop_type = "number"
                    elif isinstance(record[prop], bool):
                        prop_type = "checkbox"
                    elif isinstance(record[prop], datetime):
                        prop_type = "date"
                    elif isinstance(record[prop], list):
                        prop_type = "multi_select"
                    logger.info(f"Creating property '{prop}' with type '{prop_type}'")
                    self.add_property(prop, prop_type)

        for record in records:
            update_record = {}
            for prop, value in record.items():
                if prop in properties_map:
                    update_record[properties_map[prop]] = value
                    print(f"Mapping '{prop}' to '{properties_map[prop]}'")
                else:
                    print(f"Property '{prop}' not found in database properties.")

            if update_record:
                print(f"Creating record: {update_record}")
                self.create(update_record)

    def load_database(self, database_id: str):
        """Load the database.

        Args:
            database_id (str): Database ID
        """
        self.database_id = database_id

        try:
            self.database_info: Dict[str, Any] = self.n_client.client.databases.retrieve(database_id=database_id)
            self.title = self.database_info["title"]
            parent_type = self.database_info["parent"]["type"]
            if parent_type == "page_id":
                self.parent = BaseNotionPage(token=self.token, page_id=self.database_info["parent"][parent_type], load=False)
        except Exception as e:
            raise ValueError(f"Database with ID '{database_id}' not found.") from e

        self.database: Database[self.DataClass] = Database(self.DataClass, database_id=database_id, client=self.n_client.client)

        if self.database is None:
            raise ValueError(f"Fail to load Database on valid ID '{database_id}'.")

        self.properties = self.database_info["properties"]

        for page in self.database:
            self.pages.append(BaseNotionPage(token=self.token, page_id=page.id, load=False))

    def get_properties(self) -> Dict[str, Any]:
        """Get the database properties.

        Returns:
            Dict[str, Any]: Database Properties
        """
        self.database_info: Dict[str, Any] = self.n_client.client.databases.retrieve(database_id=self.database_id)
        self.properties = self.database_info["properties"]
        return self.properties

    # "Tasks": {
    #     "id": "%3AVpi",
    #     "name": "Tasks",
    #     "type": "relation",
    #     "relation": {
    #         "database_id": "ac1f2415-2252-4961-b983-b28817e0ef7a",
    #         "type": "single_property",
    #         "single_property": {}
    #     }
    # },
    def add_property(self, prop_name: str, prop_type: Optional[str] = "rich_text", prop_info: Optional[Dict[str, Any]] = None):
        if prop_type not in DATABASE_PROPERTIES:
            raise ValueError(f"Invalid property type '{prop_type}'.")
        if prop_info is None:
            prop_info = {}
        properties_update = {
            "type": prop_type,
            prop_type: prop_info,
        }
        self.n_client.client.databases.update(self.database_id, properties={prop_name: properties_update})

    def remove_property(self, prop_name: str):
        try:
            self.n_client.client.databases.update(self.database_id, properties={prop_name: None})
        except Exception:
            logger.error(f"Failed to remove property '{prop_name}' from database '{self.database_id}'.")

    def get_children(self, force: bool = False) -> List[BaseNotionPage]:
        return self.get_pages(force=force)

    def get_pages(self, force: bool = False) -> List[BaseNotionPage]:
        """Get Pages."""
        if force or not self.pages:
            for page in self.database:
                self.pages.append(BaseNotionPage(token=self.n_client.token, page_id=page.id, load=False))
        return self.pages

    # def new(self, parent: Optional[BaseNotionPage] = None, **kwargs) -> NotionObject:
    #     """Create a new Database Entry."""
    #     if parent is None and self.parent is None:
    #         raise ValueError("Parent BaseNotionPage must be provided.")
    #     if parent is None:
    #         parent = self.parent
    #     return self.database.new(parent=parent.page_id, **kwargs)
    def check_if_exists(self, title: str) -> bool:
        """Check if Database Entry Exists."""
        for page in self.pages:
            if page.title == title:
                return True

    def create(self, properties: Optional[Dict[str, Any]] = None, obj: Optional[NotionObject] = None) -> NotionObject:
        """Create Database Entry."""
        if properties is None and obj is None:
            raise ValueError("Either properties or obj must be provided.")
        if properties is not None and obj is not None:
            raise ValueError("Only one of properties or obj can be provided.")
        # for prop_name, prop_info in properties.items():
        #     if prop_name not in self.database.properties:
        #         raise ValueError(f"Property '{prop_name}' not found in database properties.")

        if obj is not None:
            entry = obj
        else:
            entry = self.DataClass.new(**properties)

        # if self.check_if_exists(entry):
        #     logger.warning(f"Entry '{entry.ref}' already exists in database.")
        #     db_entry = next((page for page in self.pages if page.title == entry.ref), None)
        #     return db_entry

        db_entry = self.database.create(entry)
        self.pages.append(BaseNotionPage(token=self.token, page_id=db_entry.id, load=False))
        return db_entry

    def read(self, entry_id: str) -> NotionObject:
        """Read Database Entry."""
        return self.database.find_by_id(entry_id)

    def update(self, entry: NotionObject, properties: Optional[Dict[str, Any]] = None) -> NotionObject:
        """Update Database Entry."""
        for k, v in properties.items():
            setattr(entry, k, v)
        self.database.update(entry)
        return entry

    def delete(self, entry: NotionObject):
        """Delete Database Entry."""
        self.n_client.client.blocks.delete(block_id=entry.id)
        self.pages.remove(entry)

    def delete_all(self):
        """Remove Pages."""
        for page in self.pages:
            self.n_client.client.blocks.delete(block_id=page.page_id)
            self.pages.remove(page)

    def __repr__(self):
        return f"NotionDatabase(title={self.database.title}, database_id={self.database.database_id})"

    def __iter__(self):
        return iter(self.database)

    def query(self, filter: Optional[dict] = None) -> List[NotionObject]:
        results = self.database.query(filter=filter)
        pages: List[BaseNotionPage] = []
        for result in results:
            if isinstance(result, dict):
                pages.append(BaseNotionPage(token=self.token, page_id=result["id"], load=False))
            else:
                print(f"result not dict: {type(result)}")

    def download_database(self, database_id: str, out_dir: Union[str, Path] = "./json"):
        """Download the notion database and associated pages."""
        # out_dir = Path(out_dir)
        # out_dir.mkdir(parents=True, exist_ok=True)
        # path = out_dir / "database.json"
        # prev = {pg["id"]: pg["last_edited_time"] for pg in self.io.load(path)}
        # pages = self.notion.get_database(database_id)  # download database
        # self.io.save(pages, path)

        # for cur in pages:  # download individual pages in database IF updated
        #     if prev.get(cur["id"], datetime(1, 1, 1, tzinfo=cur["last_edited_time"].tzinfo)) < cur["last_edited_time"]:
        #         self.download_page(cur["id"], out_dir / f"{cur['id']}.json", False)
        #         logger.info(f"Downloaded {cur['url']}")
