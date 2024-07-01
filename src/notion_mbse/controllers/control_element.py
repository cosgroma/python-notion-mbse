#!/usr/bin/env python
"""
@package   control_element
Details:
Created:   Sunday, June 30th 2024, 8:37:38 pm
-----
Last Modified: 06/30/2024 08:44:53
Modified By: Mathew Cosgrove
-----
"""

__author__ = "Mathew Cosgrove"
__file__ = "control_element.py"
__version__ = "0.1.0"

from typing import Any
from typing import Dict
from typing import Optional

from pydantic import Field

from ..models import Element
from .base_controller import BaseController


class ControllableElement(Element):
    """A controllable element is an element that can be controlled by a controller. It contains information about the controller that manages the element in the database.

    Attributes:
        controller (Optional[BaseController]): The controller that manages the element in the database.

    Class Methods:
        from_element: Converts an element to a controllable element.
        from_dict: Converts a dictionary to a controllable element.

    Methods:
        use_controller: Sets the controller that manages the element in the database.
        to_element: Converts the controllable element to an element.
        to_dict: Converts a controllable element to a dictionary.
        create: Creates the element in the database.
        update: Updates the element in the database.
        read: Reads the element from the database.
        delete: Deletes the element from the database.

    Raises:
        ValueError: If the element has no controller to create, update, read, or delete.
    """

    controller: Optional[BaseController] = Field(None, description="The controller that manages the element in the database.")

    @classmethod
    def from_element(cls, element: Element):
        """Converts an element to a controllable element.

        Args:
            element (Element): The element to convert.

        Returns:
            ControllableElement: The controllable element.
        """
        return cls(**element.model_dump())

    @classmethod
    def from_dict(cls, element_dict: Dict[str, Any]):
        """Converts a dictionary to a controllable element.

        Args:
            element_dict (Dict[str, Any]): The dictionary to convert.

        Returns:
            ControllableElement: The controllable element.
        """
        return cls(**element_dict)

    def use_controller(self, controller: BaseController):
        """Sets the controller that manages the element in the database.

        Args:
            controller (BaseController): The controller that manages the element in the database.
        """
        self.controller = controller

    def to_element(self) -> Element:
        """Converts the controllable element to an element.

        Returns:
            Element: The element.
        """
        return Element(**self.model_dump())

    def to_dict(self):
        """Converts a controllable element to a dictionary.

        Returns:
            Dict[str, Any]: The dictionary.
        """
        return self.model_dump()

    def create(self) -> bool:
        """Creates the element in the database.

        Raises:
            ValueError: If the element has no controller to create.

        Returns:
            bool: True if the element was created successfully, False otherwise.
        """
        if self.controller is not None:
            obj = self.controller.create(self.to_element())
            self.set_with_element(obj)
            return True
        else:
            raise ValueError("Element has no controller to create")

    def update(self) -> bool:
        """Updates the element in the database.

        Raises:
            ValueError: If the element has no controller to update.

        Returns:
            bool: True if the element was updated successfully, False otherwise.
        """
        if self.controller is not None:
            self.controller.update(self.to_element())
            return True
        else:
            raise ValueError("Element has no controller to update")

    def read(self) -> bool:
        """Reads the element from the database.

        Raises:
            ValueError: If the element has no controller to read.

        Returns:
            bool: True if the element was read successfully, False otherwise.
        """
        if self.controller is not None:
            obj = self.controller.read(self.to_element())
            if obj is not None:
                self.set_with_element(obj)
                return True
            return False
        else:
            raise ValueError("Element has no controller to read")

    def delete(self) -> bool:
        """Deletes the element from the database.

        Raises:
            ValueError: If the element has no controller to delete.

        Returns:
            bool: True if the element was deleted successfully, False otherwise.
        """
        if self.controller is not None:
            self.controller.delete(self)
            return True
        else:
            raise ValueError("Element has no controller to delete")
