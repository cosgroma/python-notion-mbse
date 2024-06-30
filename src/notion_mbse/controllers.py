#!/usr/bin/env python
"""
@package   controllers
Details:
Created:   Sunday, June 30th 2024, 1:52:47 pm
-----
Last Modified: 06/30/2024 02:18:45
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "controllers.py"
__version__ = "0.1.0"

import json
from pathlib import Path
from pprint import pprint
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import Union

from databasetools.adapters.notion import NotionClient
from databasetools.adapters.notion import NotionDatabase
from notion_objects import Page
from pydantic import ValidationError
from pymongo.collection import Collection
from pymongo.errors import PyMongoError

from .base_controller import BaseController
from .base_controller import T
from .models import PydanticObjectId


class MongoCollectionController(BaseController[T]):
    """A generic controller that can be used to perform CRUD operations on a MongoDB collection.

    Attributes:
        collection (Collection): The MongoDB collection to perform operations on.

    Methods:
        create(document_data: Dict[str, Any]) -> T:
            Creates a new document in the collection.
        read(query: Dict[str, Any]) -> List[T]:
    """

    def __init__(self, collection: Collection, model: Type[T]):
        """Initializes the generic controller.

        Parameters:
            collection (Collection): The MongoDB collection to perform operations on.
        """
        self.collection: Collection = collection
        self._model: Type[T] = model

    @property
    def model(self) -> Type[T]:
        return self._model

    @model.setter
    def model(self, model: Type[T]):
        self._model = model

    # @abstractmethod
    # def create(self, element: T) -> T:
    def create(self, item: Union[Dict[str, Any], T]) -> T:
        """
        Creates a new document in the collection.

        Parameters:
            item (Union[Dict[str, Any], T]): The document data to create.

        Returns:
            T: The created document as a Pydantic model instance.
        """
        try:
            if isinstance(item, dict):
                document = self.model(**item)
            elif isinstance(item, self.model):
                document = item
            else:
                raise ValueError(f"Item must be a dictionary or an instance of {self.model}")

            result = self.collection.insert_one(document.model_dump())

            if not result.acknowledged:
                raise PyMongoError("Insert operation not acknowledged by MongoDB.")
            return document

        except ValidationError as e:
            # Handle validation errors
            print(f"Validation error: {e}")
            raise
        except PyMongoError as e:
            # Handle MongoDB errors
            print(f"Database error: {e}")
            raise

    # @abstractmethod
    def read(self, element: T) -> Optional[T]:
        """
        Reads a document from the collection.

        Parameters:
            element (T): The document to read.

        Returns:
            T: The document as a Pydantic model instance.
        """
        document = self.collection.find_one({"id": element.id})
        if not document:
            return None
        pprint(document)
        document["id"] = PydanticObjectId(document["id"])
        return self.model(**document)

    # @abstractmethod
    # def get(self, query: Dict[str, Any]) -> Optional[T]:

    def get(self, query: Dict[str, Any]) -> Optional[T]:
        """
        Fetches a document from the collection based on a query.

        Parameters:
            query (Dict[str, Any]): The query to filter documents.

        Returns:
            Optional[T]: The document as a Pydantic model instance, or None if not found.
        """
        document = self.collection.find_one(query)
        return self.model(**document) if document else None

    # @abstractmethod
    # def read_all(self, query: Dict[str, Any]) -> List[T]:
    def read_all(self, query: Dict[str, Any], limit: Optional[int] = None) -> Optional[List[T]]:
        """
        Reads documents from the collection.

        Parameters:
            query (Dict[str, Any]): The query to filter documents.

        Returns:
            List[T]: A list of document instances as Pydantic model objects.
        """
        try:
            documents = self.collection.find(query).limit(limit) if limit else self.collection.find(query)
            return [self.model(**doc) for doc in documents]
        except ValidationError as e:
            raise ValidationError(f"Validation error: {e}") from e
        except PyMongoError as e:
            raise PyMongoError(f"Database error: {e}") from e
        except Exception as e:
            raise Exception(f"Error: {e}") from e

    # @abstractmethod
    # def update(self, element: T) -> bool:
    def update(self, element: Union[Dict[str, Any], T]) -> bool:
        """
        Updates documents in the collection.

        Parameters:
            query (Dict[str, Any]): The query to filter documents to update.
            update (Union[Dict[str, Any], T]): The update data.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        # {"id": conversation.id}
        if isinstance(element, dict):
            update_data = element
        elif isinstance(element, self.model):
            update_data = element.model_dump()
        result = self.collection.update_one({"id": element.id}, {"$set": update_data})
        return result.modified_count > 0

    # @abstractmethod
    # def update_many(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> bool:
    def update_many(self, query: Dict[str, Any], update: Union[Dict[str, Any], T]) -> bool:
        """
        Updates documents in the collection.

        Parameters:
            query (Dict[str, Any]): The query to filter documents to update.
            update (Union[Dict[str, Any], T]): The update data.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if isinstance(update, dict):
            update_data = update
        elif isinstance(update, self.model):
            update_data = update.model_dump()
        result = self.collection.update_many(query, {"$set": update_data})
        return result.modified_count > 0

    # @abstractmethod
    # def delete(self, element: T) -> bool:
    def delete(self, element: Union[Dict[str, Any], T]) -> bool:
        """
        Deletes documents from the collection.

        Parameters:
            query (Dict[str, Any]): The query to filter documents to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        if isinstance(element, dict):
            result = self.collection.delete_one(element)
        elif isinstance(element, self.model):
            result = self.collection.delete_one({"id": element.id})
        return result.deleted_count > 0

    def delete_all(self):
        """
        Deletes all documents from the collection.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        result = self.collection.delete_many({})
        return result.deleted_count > 0

    def delete_item(self, item: Union[Dict[str, Any], T]) -> bool:
        """
        Deletes a single document from the collection.

        Parameters:
            item (Union[Dict[str, Any], T]): The document to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        if isinstance(item, dict):
            query = item
        elif isinstance(item, self.model):
            query = item.model_dump()
        else:
            raise ValueError("Item must be a dictionary or an instance of the model.")
        result = self.collection.delete_one(query)
        return result.deleted_count > 0

    def __iter__(self) -> "MongoCollectionController":
        """Returns an iterator object"""
        self._cursor = self.collection.find()
        return self

    def __next__(self) -> T:
        try:
            # Attempt to get the next document from the cursor
            document = next(self._cursor)
        except StopIteration:
            # If there are no more documents, raise StopIteration to stop the iteration
            raise StopIteration from None

        # Convert the document to a Pydantic model instance
        return self.model(**document)

    def __len__(self):
        return self.collection.count_documents({})

    def __repr__(self):
        return f"MongoCollectionController(collection={self.collection}, model={self.model})"

    def save_all_to_json(self, file_path: str) -> str:
        """
        Saves all documents in the collection to a JSON file.

        Parameters:
            file_path (str): The path to save the JSON file.
        """
        documents: List[T] = self.read({})
        json_array = [doc.model_dump() for doc in documents]
        with Path.open(file_path, "w") as file:
            json.dump(json_array, file, indent=4)
        return file_path


class NotionDatabaseController(BaseController[T]):
    def __init__(self, token: str, database_id: Optional[str] = None, DataClass: Optional[Type[T]] = None):
        super().__init__()
        self.token = token
        self.n_client = NotionClient(token=token)
        self.database_id = database_id
        self.DataClass = DataClass or Page  # Default to Page if no DataClass provided
        self._db = NotionDatabase(token=token, database_id=self.database_id, DataClass=self.DataClass)

    def create(self, element: Type[T]) -> T:
        # Implementation specific to Notion
        return self._db.create(obj=element)

    def read(self, query: Dict[str, Any]) -> List[T]:
        # Implementation specific to Notion
        return self._db.read(query["id"])

    def update(self, element: Type[T]) -> bool:
        # Implementation specific to Notion
        return self._db.update(element, properties=element.model_dump())

    def delete(self, obj: Type[T]) -> bool:
        # Implementation specific to Notion
        self._db.delete(obj)

    def __iter__(self) -> List[T]:
        # Specific to Notion
        return iter(self._db.get_pages())

    def __repr__(self):
        return f"NotionDatabaseController(db_id={self.database_id})"
