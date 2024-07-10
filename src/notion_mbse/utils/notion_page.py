#!/usr/bin/env python
"""
@package   notion_page
Details:
Created:   Saturday, July 6th 2024, 3:34:54 pm
-----
Last Modified: 07/09/2024 05:29:47
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "notion_page.py"
__version__ = "0.1.0"

import os
from pathlib import Path
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from notion_objects import Page

# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.DiGraph()
from .notion_base import BaseNotionPage
from .notion_client_extend import NotionClient
from .notion_database import NotionDatabase
from .notion_utils import find_title_prop
from .notion_utils import get_title_content
from .notion_utils import logger
from .notion_utils import slugify

NOTION_API_KEY = os.getenv("NOTION_API_KEY", None)


class NotionPage(BaseNotionPage):
    def __init__(
        self,
        token: Optional[str] = None,
        page_id: Optional[str] = None,
        parent: Optional["NotionPage"] = None,
        load: bool = False,
        recursive: bool = False,
    ):
        if NOTION_API_KEY:
            token = NOTION_API_KEY
        if token is None:
            raise ValueError("No token provided.")

        self.token = token
        self.n_client = NotionClient(token)

        self.page_id = page_id
        self.parent = parent
        self.title = None

        self.blocks: List[dict] = []
        self.children: List[Union[NotionPage, NotionDatabase]] = []
        self.child_pages: List[NotionPage] = []
        self.child_databases: List[NotionDatabase] = []

        self.page_results: dict = {}
        self.page = None
        self.parent = None

        self.get_page()

        if load:
            self.get_blocks()

        if recursive:
            self.get_children(recursive=recursive)

        self.local_dir = Path.cwd()
        self.file_path = None

        if self.title:
            self.basename = slugify(self.title)

    @property
    def name(self):
        return self.title

    def set_local_dir(self, local_dir: Union[str, Path]):
        """Set the local directory for saving files.

        Args:
            local_dir (Union[str, Path]): Local Directory

        """
        self.local_dir = Path(local_dir)

    def get_file_path(self) -> Path:
        """Get the file path for saving the page.

        Returns:
            Path: File Path
        """
        return self.file_path

    def set_file_path(self, file_name: Union[str, Path]):
        self.file_path = self.local_dir / file_name
        self.file_type = self.file_path.suffix[1:]

    def save(self, type: str = "json", recursive: bool = False, file_name: Optional[str] = None, parent_name: Optional[str] = None) -> Path:
        """Save the page as a file.

        Args:
            type (str, optional): File Type. Defaults to "json".
            recursive (bool, optional): Save recursively. Defaults to False.
            file_name (Optional[str], optional): File Name. Defaults to None.
            parent_name (Optional[str], optional): Parent Name. Defaults to None.

        Returns:
            Path: File Path
        """
        if self.page_id is None:
            raise ValueError("Page ID is not provided.")
        metadata = self.n_client.get_metadata(self.page_id)
        metadata_filename = self.local_dir / "page_metadata.json"
        self.n_client.save([metadata], metadata_filename)
        logger.info(f"Saved metadata to {metadata_filename}")

        if len(self.blocks) == 0:
            self.get_blocks()
            if len(self.blocks) == 0:
                raise ValueError("No blocks found.")

        if file_name is not None:
            self.set_file_path(file_name)

        if self.file_path is None:
            file_name = f"{slugify(self.title)}.{type}"
            self.set_file_path(file_name)

        #  def get_post_metadata(self, post):
        # converter = JsonToMd(config={"apply_list": {"delimiter": ","}})
        # return {key: self.get_key(converter.json2md(value)) for key, value in post["properties"].items() if converter.json2md(value)}
        # markdown = JsonToMd(metadata).page2md(blocks)

        self.save(self.blocks, self.file_path)
        if recursive:
            for page in self.child_pages:
                page.save(type=type, recursive=True)

        logger.info(f"Saved blocks to {self.file_path}")
        return self.file_path

    def get_page(self, force: bool = False) -> Tuple[Page, dict]:
        """Get a page."""
        if self.page_id is None:
            raise ValueError("Page ID is not provided.")
        if force or not self.page:
            self.page_results = self.n_client.client.pages.retrieve(page_id=self.page_id)
            self.page = Page(self.page_results)

            if self.page_results["parent"]["type"] != "database_id":
                title_prop = "title"
            else:
                title_prop = find_title_prop(self.page_results["properties"])
            # get_title_content
            self.title = get_title_content(self.page_results["properties"][title_prop])

        return self.page, self.page_results

    def get_blocks(self, force: bool = False) -> List[dict]:
        """Get all blocks in a page.

        Args:
            force (bool, optional): Force Refresh. Defaults to False.

        Returns:
            List[dict]: List of Blocks
        """
        if force or not self.blocks:
            self.blocks = self.n_client.get_blocks(self.page_id)
        return self.blocks

    def set_blocks(self, blocks: List[dict], clear: bool = False):
        """Set all blocks in a page.

        Args:
            blocks (List[dict]): List of Blocks
            clear (bool, optional): Clear Existing Blocks. Defaults to False.


        """
        if clear:
            self.clear_blocks()
        if not blocks:
            raise ValueError("No blocks provided.")
        if not isinstance(blocks, list):
            raise ValueError("Blocks must be a list.")
        if len(blocks) == 0:
            raise ValueError("Blocks must not be empty.")
        if not isinstance(blocks[0], dict):
            raise ValueError("Blocks must be a list of dictionaries.")

        self.n_client.client.blocks.children.append(block_id=self.page_id, children=blocks)

    def clear_blocks(self):
        """Clear all blocks in a page."""

        blocks = self.get_blocks(force=True)
        for block in blocks:
            self.n_client.client.blocks.delete(block_id=block["id"])

    def add_page(self, title: str) -> "NotionPage":
        """Add a page to the current page.

        Args:
            title (str): Page Title

        Returns:
            NotionPage: Notion Page
        """
        page = self.n_client.client.pages.create(
            parent={"page_id": self.page_id},
            properties={"title": [{"text": {"content": title}}]},
        )
        return NotionPage(token=self.n_client.token, page_id=page["id"], load=False)

    def add_database(self, title: str) -> NotionDatabase:
        """Add a database to the current page."""
        database = self.n_client.client.databases.create(
            parent={"page_id": self.page_id}, title=[{"text": {"content": title}}], properties={"Name": {"title": {}}}
        )
        return NotionDatabase(token=self.n_client.token, database_id=database["id"])

    def get_children(self, force: bool = False, recursive: bool = False) -> List[Union["NotionPage", NotionDatabase]]:
        """Get children of a page."""
        if force or not self.children:
            try:
                blocks = self.get_blocks()
                for block in blocks:
                    if block["type"] == "child_page":
                        self.children.append(NotionPage(token=self.n_client.token, page_id=block["id"], load=False, recursive=recursive))
                    elif block["type"] == "child_database":
                        self.children.append(NotionDatabase(token=self.n_client.token, database_id=block["id"]))
            except Exception as e:
                logger.error(f"Error: {e}")
        return self.children

    def get_child_pages(self, force: bool = False) -> List["NotionPage"]:
        """Get Child Pages.

        Args:
            page_id (str): Page ID

        Returns:
            List[dict]: List of Child Pages
        """

        if force or not self.child_pages:
            try:
                blocks = self.get_blocks()
                for block in blocks:
                    if block["type"] == "child_page":
                        self.child_pages.append(NotionPage(token=self.n_client.token, page_id=block["id"], load=False))
            except Exception as e:
                logger.error(f"Error: {e}")
        return self.child_pages

    def get_child_databases(self, force: bool = False) -> List[NotionDatabase]:
        """Get Child Databases.

        Args:
            force (bool, optional): Force Refresh. Defaults to False.

        Returns:
            List[dict]: List of Child Databases
        """
        if force or not self.child_databases:
            blocks = self.get_blocks()
            for block in blocks:
                if block["type"] == "child_database":
                    self.child_databases.append(NotionDatabase(token=self.n_client.token, database_id=block["id"]))
        return self.child_databases

    def delete_child_pages(self):
        """Delete Child Pages."""
        for page in self.child_pages:
            self.n_client.client.blocks.delete(block_id=page.page_id)
            self.child_pages.remove(page)

    def delete_page(self):
        """Delete Page."""
        if self.page_id:
            self.n_client.client.blocks.delete(block_id=self.page_id)
        else:
            raise ValueError("No page ID provided.")

    def __repr__(self):
        return f"NotionPage(title={self.title}, page_id={self.page_id})"

    def info(self):
        return {
            "title": self.title,
            "page_id": self.page_id,
            "parent": self.parent,
            "blocks": self.blocks,
            "children": self.children,
            "child_pages": self.child_pages,
            "child_databases": self.child_databases,
            "local_dir": self.local_dir,
        }
