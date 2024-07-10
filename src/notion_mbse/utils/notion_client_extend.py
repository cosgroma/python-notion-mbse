#!/usr/bin/env python
"""
@package   notion_client
Details:
Created:   Saturday, July 6th 2024, 3:35:34 pm
-----
Last Modified: 07/09/2024 05:31:27
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "notion_client.py"
__version__ = "0.1.0"

import json
import os
from abc import ABC
from abc import abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import dotenv
from notion_client import Client
from notion_client.helpers import iterate_paginated_api as paginate
from notion_objects import NotionObject
from notion_objects import Page

from .notion_utils import logger
from .notion_utils import normalize_id

dotenv.load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY", None)


class BaseTransformer(ABC):
    key: str = ""

    @abstractmethod
    def forward(self, blocks: List[dict]) -> List[dict]: ...

    @abstractmethod
    def reverse(self, o: Any) -> Union[None, str]: ...


class LastEditedToDateTime(BaseTransformer):
    key = "last_edited_time"
    key_type = datetime

    def forward(self, blocks) -> List:
        """Convert last_edited_time to datetime object.
        Args:
            blocks (List[dict]): List of blocks

        Returns:
            List: List of blocks with last_edited_time as datetime object
        """
        key = self.key
        return [
            {
                **block,
                key: datetime.fromisoformat(block[key][:-1]),
                "id": normalize_id(block["id"]),
            }
            for block in blocks
        ]

    def reverse(self, o: Any) -> Union[None, str]:
        """Convert datetime object to string.
        Args:
            o (Any): Object
        Returns:
            Union[None, str]: String representation of datetime object
        """
        if isinstance(o, datetime):
            return o.isoformat() + "Z"


class NotionClient:
    """
    A client for interacting with Notion pages and databases.

    This class provides methods to retrieve metadata, recent pages, projects, page blocks, and databases from the Notion API.

    Attributes:
        token (str): The authentication token for accessing the Notion API.
        filter (Optional[dict]): Optional filter for database queries.
        client (Client): The Notion client object.
        transformer (LastEditedToDateTime): Utility for transforming date-time fields.

    Methods:
        load(path: Union[str, Path]) -> List[dict]:
            Loads data from a file and transforms it using the transformer.

        save(blocks: List[dict], path: Union[str, Path], overwrite: bool = False):
            Saves the given blocks to a file.

        get_blocks(block_id: int) -> List:
            Retrieves all page blocks as JSON. Recursively fetches descendants.

        get_database(database_id: str) -> List:
            Fetches pages in a database as JSON.

        get_metadata(page_id: str) -> Dict[str, Any]:
            Retrieves metadata of a specific page.

        get_recent_pages() -> List[Dict[str, Any]]:
            Retrieves a list of recent pages via a search query.

        download_url(url: str, out_dir: Union[str, Path] = "./json"):
            Downloads the Notion page or database from a URL and saves it as JSON.

        download_page(page_id: str, out_path: Union[str, Path] = "./json", fetch_metadata: bool = True):
            Downloads a specific Notion page and its blocks. Metadata is optionally fetched and saved.

        download_database(database_id: str, out_dir: Union[str, Path] = "./json"):
            Downloads all pages and data from a specified Notion database.

    Example Usage:
    --------------
    ```python
    client = NotionClient(token="your-notion-api-token")

    # Retrieve metadata for a specific page
    page_metadata = client.get_metadata(page_id="your-page-id")

    # Fetch recent pages
    recent_pages = client.get_recent_pages()
    ```
    """

    def __init__(self, token: Optional[str], transformer: Optional[LastEditedToDateTime] = None, filter: Optional[dict] = None):
        if not token:
            if NOTION_API_KEY is None:
                raise ValueError("NOTION_API_KEY is not set")
            token = NOTION_API_KEY
        self.token = token
        self.filter = filter
        self.client = Client(auth=token)
        self.transformer = transformer if transformer else LastEditedToDateTime()

    def load(self, path: Union[str, Path]) -> List[dict]:
        """
        Load data from a file and transform it using the transformer.

        Args:
            path (Union[str, Path]): The path to the file.

        Returns:
            List[dict]: The transformed data as a list of dictionaries.
        """
        if isinstance(path, str):
            path = Path(path)
        if path.exists():
            with Path.open(path) as f:
                return self.transformer.forward(json.load(f))
        return []

    def save(self, blocks: List[dict], path: Union[str, Path], overwrite: bool = False):
        """
        Save the given blocks to a file.

        Args:
            blocks (List[dict]): The blocks to save.
            path (Union[str, Path]): The path to save the file.
            overwrite (bool, optional): Whether to overwrite the file if it already exists. Defaults to False.

        Raises:
            ValueError: If there are no blocks to save, if blocks is not a list, or if blocks is not a list of dictionaries.
            ValueError: If no path is provided.
            FileExistsError: If the file already exists and overwrite is set to False.
        """
        if not blocks:
            raise ValueError("No blocks to save.")
        if not isinstance(blocks, list):
            raise ValueError("Blocks must be a list.")
        if not isinstance(blocks[0], dict):
            raise ValueError("Blocks must be a list of dictionaries.")
        if not path:
            raise ValueError("No path provided.")
        path = Path(path)
        if path.exists() and not overwrite:
            raise FileExistsError(f"File already exists: {path}")

        with Path.open(path, "w") as f:
            json.dump(blocks, f, default=self.transformer.reverse, indent=4)

    def get_metadata(self, page_id: str) -> Dict[str, Any]:
        """Get page metadata.

        Args:
            page_id (str): Page ID

        Returns:
            Dict[str, Any]: Page Metadata
        """
        if not page_id:
            raise ValueError("Page ID is required.")
        results = self.client.pages.retrieve(page_id=page_id)
        if results:
            return self.transformer.forward([results])[0]
        return {}

    def get_recent_pages(
        self, query: Optional[str] = None, as_objects: Optional[bool] = False
    ) -> Union[List[Dict[str, Any]], List[NotionObject]]:
        """Get Recent Pages via Search Query.

        Returns:
            List[Dict[str, Any]]: List of Recent Pages
        """
        payload = {
            "filter": {
                "value": "page",
                "property": "object",
            },
            "sort": {
                "direction": "descending",
                "timestamp": "last_edited_time",
            },
        }
        if query:
            payload["query"] = query

        results = self.client.search(**payload).get("results")
        if as_objects:
            return [Page.new(**page) for page in results]
        else:
            return results

    def get_recent_blocks(self, query: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get Recent Blocks by getting recent pages then fetching blocks.

        Returns:
            List[Dict[str, Any]]: List of Recent Blocks
        """
        payload = {
            "filter": {
                "value": "page",
                "property": "object",
            },
            "sort": {
                "direction": "descending",
                "timestamp": "last_edited_time",
            },
        }
        if query:
            payload["query"] = query

        return self.client.search(**payload).get("results")

    def get_blocks(self, block_id: int) -> List:
        """Get all page blocks as json. Recursively fetches descendants.

        Args:
            block_id (int): Block ID

        Returns:
            List: List of page blocks
        """
        blocks = []
        results = paginate(self.client.blocks.children.list, block_id=block_id)
        for child in results:
            try:
                child["children"] = list(self.get_blocks(child["id"])) if child["has_children"] else []
                blocks.append(child)
            except Exception as e:
                logger.error(f"Error: {e}")

        return list(self.transformer.forward(blocks))

    def get_database(self, database_id: str) -> List:
        """Fetch pages in database as json."""
        if self.filter:
            results = paginate(
                self.client.databases.query,
                database_id=database_id,
                filter=self.filter,
            )
        else:
            results = paginate(
                self.client.databases.query,
                database_id=database_id,
            )
        pages = [self.client.pages.retrieve(page_id=pg["id"]) for pg in results]
        return list(self.transformer.forward(pages))

    def download_url(self, url: str, out_dir: Union[str, Path] = "./json"):
        """Download the notion page or database."""
        out_dir = Path(out_dir)
        slug = url.split("/")[-1].split("?")[0]
        if "-" in slug:
            page_id = slug.split("-")[-1]
            self.download_page(page_id, out_dir / f"{page_id}.json")
        else:
            self.download_database(slug, out_dir)

    def download_page(self, page_id: str, out_path: Union[str, Path] = "./json", fetch_metadata: bool = True):
        """Download the notion page."""
        out_path = Path(out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        blocks = self.get_blocks(page_id)
        self.save(blocks, out_path)

        if fetch_metadata:
            metadata = self.get_metadata(page_id)
            self.save([metadata], out_path.parent / "database.json")

    def download_database(self, database_id: str, out_dir: Union[str, Path] = "./json"):
        """Download the notion database and associated pages."""
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / "database.json"
        prev = {pg["id"]: pg["last_edited_time"] for pg in self.load(path)}
        pages = self.get_database(database_id)  # download database
        self.save(pages, path)

        for cur in pages:  # download individual pages in database IF updated
            if prev.get(cur["id"], datetime(1, 1, 1, tzinfo=cur["last_edited_time"].tzinfo)) < cur["last_edited_time"]:
                self.download_page(cur["id"], out_dir / f"{cur['id']}.json", False)
                logger.info(f"Downloaded {cur['url']}")

    def covert_init(self, token: str, strip_meta_chars: Optional[str] = None, extension: str = "md", filter: Optional[dict] = None):
        ...
        # self.converter = JsosnToMdConverter(strip_meta_chars=strip_meta_chars, extension=extension)

    def export_url(self, url: str, json_dir: Union[str, Path] = "./json", md_dir: Union[str, Path] = "./md") -> Path:
        """Export the notion page or database."""
        self.download_url(url, json_dir)
        # return self.converter.convert(json_dir, md_dir)

    def export_database(self, database_id: str, json_dir: Union[str, Path] = "./json", md_dir: Union[str, Path] = "./md") -> Path:
        """Export the notion database and associated pages."""
        self.download_database(database_id, json_dir)
        # return self.converter.convert(json_dir, md_dir)

    def export_page(self, page_id: str, json_dir: Union[str, Path] = "./json", md_dir: Union[str, Path] = "./md"):
        """Export the notion page."""
        json_dir_path = Path(json_dir)
        self.download_page(page_id, json_dir_path / f"{page_id}.json")
        # return self.converter.convert(json_dir, md_dir)

    def move_page_to_new_db(self, page_id: str, new_db_id: str):
        """Move a page to a new database."""
        self.client.pages.update(page_id=page_id, parent={"database_id": new_db_id})

    def move_db_to_page(self, db_id: str, page_id: str):
        """Move a database to a page."""
        self.client.databases.update(database_id=db_id, parent={"page_id": page_id})
