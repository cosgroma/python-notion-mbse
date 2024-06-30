#!/usr/bin/env python
"""
@package   base_controller
Details:
Created:   Saturday, June 29th 2024, 7:36:06 pm
-----
Last Modified: 06/30/2024 01:52:29
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "base_controller.py"
__version__ = "0.1.0"

from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import Generic
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseController(ABC, Generic[T]):
    """
    Abstract base class for database controllers.
    """

    @property
    @abstractmethod
    def model(self) -> Type[T]:
        """
        This should return the model class that the controller works with.
        """
        raise NotImplementedError

    @abstractmethod
    def create(self, element: T) -> T:
        """
        Create a new entry in the database.
        """
        raise NotImplementedError

    @abstractmethod
    def read(self, element: T) -> T:
        """
        Read the  from the database based on a query.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, query: Dict[str, Any]) -> Optional[T]:
        """
        Fetch an entry from the database based on a query.
        """
        # Implementation fetching data from the database
        raise NotImplementedError

    @abstractmethod
    def read_all(self, query: Dict[str, Any]) -> List[T]:
        """
        Read all entries from the database.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, element: T) -> bool:
        """
        Update an entry in the database.
        """
        raise NotImplementedError

    @abstractmethod
    def update_many(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> bool:
        """
        Update all entries in the database based on a query.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, element: T) -> bool:
        """
        Delete an entry from the database.
        """
        raise NotImplementedError

    @abstractmethod
    def __iter__(self):
        """
        Iterate over all entries in the database.
        """
        raise NotImplementedError

    @abstractmethod
    def __repr__(self):
        """
        Return a string representation of the database controller.
        """
        raise NotImplementedError

    def refresh(self, element: T) -> bool:
        """
        Refresh the provided element with data from the database.
        This assumes the element includes its identifier or any required keys.
        """
        query = {"id": element.id}  # Adjust the query as needed based on your schema
        updated_data = self.get(query)
        if updated_data:
            for key, value in updated_data.dict().items():
                setattr(element, key, value)
            return True
        return False

    ## Sketchy implementation of __getitem__, __setitem__, __delitem__

    def __getitem__(self, items: Union[str, List[str]]) -> T:
        """This method is used to get an item from the database.

        Args:
            attr (str): The attribute to get from the database.

        Returns:
            T: The item from the database.
        """
        if isinstance(items, str):
            return self.get({items: items})
        elif isinstance(items, list):
            return self.read_all({items: items})

    def __setitem__(self, item: T, value: Dict[str, Any]):
        if not isinstance(value, dict):
            raise ValueError("Value must be a dictionary with update data.")

        self.update(item, value)

    def __delitem__(self, item: T):
        self.delete(item)
