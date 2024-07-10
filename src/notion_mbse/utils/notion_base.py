#!/usr/bin/env python
"""
@package   notion_base
Details:
Created:   Saturday, July 6th 2024, 3:35:34 pm
-----
Last Modified: 07/06/2024 03:51:40
Modified By: Mathew Cosgrove
-----
"""

# Base classes for Notion Page and Database adapters.


class BaseNotionPage:
    def __init__(self, page_id: str, title: str, url: str):
        self.page_id = page_id
        self.title = title
        self.url = url

    # @abstractmethod
    # def get_properties(self):
    #     pass

    # @abstractmethod
    # def get_property(self, name: str):
    #     pass

    # @abstractmethod
    # def set_property(self, name: str, value):
    #     pass

    # @abstractmethod
    # def get_children(self):
    #     pass

    # @abstractmethod
    # def get_child(self, name: str):
    #     pass

    # @abstractmethod
    # def add_child(self, name: str, value):
    #     pass

    # @abstractmethod
    # def update(self):
    #     pass

    # @abstractmethod
    # def delete(self):
    #     pass


class BaseNotionDatabase:
    def __init__(self, database_id: str, title: str, url: str):
        self.database_id = database_id
        self.title = title
        self.url = url

    # @abstractmethod
    # def get_properties(self):
    #     pass

    # @abstractmethod
    # def get_property(self, name: str):
    #     pass

    # @abstractmethod
    # def set_property(self, name: str, value):
    #     pass

    # @abstractmethod
    # def get_children(self):
    #     pass

    # @abstractmethod
    # def get_child(self, name: str):
    #     pass

    # @abstractmethod
    # def add_child(self, name: str, value):
    #     pass

    # @abstractmethod
    # def update(self):
    #     pass

    # @abstractmethod
    # def delete(self):
    #     pass
