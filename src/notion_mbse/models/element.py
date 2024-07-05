from datetime import datetime
from enum import Enum
from typing import List
from typing import Optional

# from pydantic.schema import schema
from bson import ObjectId
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import field_serializer


class PydanticObjectId(ObjectId):
    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        if isinstance(v, str) and ObjectId.is_valid(v):
            return str(ObjectId(v))
        raise ValueError("Invalid ObjectId")

    @classmethod
    def __get_pydantic_json_schema__(cls, model_config, handler):
        return {"type": "string", "format": "ObjectId"}


class Element(BaseModel):
    """A base element contains common attributes that are shared by all elements. It contains information about the unique identifier, name, description, version, tags, type, sub-type, created by, created at, modified by, modified at, status, and documentation."""

    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: PydanticObjectId = Field(
        default_factory=PydanticObjectId,
        description="The unique identifier of the element.",
    )
    name: Optional[str] = Field(None, description="The name of the element.")
    description: Optional[str] = Field(None, description="The description of the element.")
    version: Optional[str] = Field(None, description="The version of the element.")
    tags: List[str] = Field([], description="The tags associated with the element.")
    type: Optional[str] = Field(None, description="The type of the element.")
    sub_type: Optional[str] = Field(None, description="The sub-type of the element.")
    created_by: Optional[str] = Field(None, description="The user who created the element.")
    created_at: datetime = Field(
        default_factory=datetime.now,
        description="The date and time the element was created.",
    )
    modified_by: Optional[str] = Field(None, description="The user who last modified the element.")
    modified_at: Optional[datetime] = Field(None, description="The date and time the element was last modified.")
    status: Optional[str] = Field(None, description="The status of the element.")
    documentation: Optional[str] = Field(None, description="The documentation associated with the element.")
    ref_ids: List[str] = Field([], description="The reference IDs associated with the element.")

    @field_serializer("modified_at")
    def serialize_dt(self, modified_at: datetime, _info):
        if modified_at is None:
            return None
        return modified_at.timestamp()

    # @field_serializer("id")
    # def serialize_id(self, id: PydanticObjectId, _info):
    #     return str(id)

    # @model_serializer
    # def ser_model(self) -> Dict[str, Any]:
    #     return {
    #         "id": str(self.id),
    #         "name": self.name,
    #         "description": self.description,
    #         "version": self.version,
    #         "tags": self.tags,
    #         "type": self.type,
    #         "sub_type": self.sub_type,
    #         "created_by": self.created_by,
    #         "created_at": self.created_at,
    #         "modified_by": self.modified_by,
    #         "modified_at": self.modified_at,
    #         "status": self.status,
    #         "documentation": self.documentation,
    #         "ref_ids": self.ref_ids
    #     }

    def set_with_element(self, element: "Element"):
        for key, value in element.model_dump().items():
            setattr(self, key, value)


class RelationshipType(Enum):
    ASSOCIATION = "Association"
    DEPENDENCY = "Dependency"
    AGGREGATION = "Aggregation"
    COMPOSITION = "Composition"
    INHERITANCE = "Inheritance"
    REALIZATION = "Realization"


class Relationship(Element):
    """A relationship between two elements.

    A relationship element represents a relationship between two elements. It contains information about the source element, target element, and the type of relationship between the two elements.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
    type: Optional[RelationshipType] = Field(None, description="The type of relationship.")
    source_element_id: PydanticObjectId = Field(description="The unique identifier of the source element.")
    target_element_id: Optional[PydanticObjectId] = Field(None, description="The unique identifier of the target element.")


# class ElementAttribute(Element):
#     """An element attribute.

#     An element attribute represents an attribute of an element. It contains information about the name, type, and value of the attribute.
#     """
#     model_config = ConfigDict(arbitrary_types_allowed=True)
#     type: Optional[str] = Field(None, description="The type of the attribute.")
#     value: Optional[str] = Field(None, description="The value of the attribute.")

# class ElementMethod(Element):
#     """An element method.

#     An element method represents a method of an element. It contains information about the name, parameters, and return type of the method.
#     """
#     model_config = ConfigDict(arbitrary_types_allowed=True)
#     parameters: Optional[List[str]] = Field([], description="The parameters of the method.")
#     return_type: Optional[str] = Field(None, description="The return type of the method.")


class ModelElementType:
    REQUIREMENT = "Requirement"
    SYSTEM_COMPONENT = "SystemComponent"
    SYSTEM_BUILD = "SystemBuild"
    BEHAVIOR = "Behavior"


class Requirement(Element):
    """A requirement element.

    A requirement element represents a requirement. It contains information about the priority, status, and verification method of the requirement.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
    priority: Optional[str] = Field(None, description="The priority of the requirement.")
    status: Optional[str] = Field(None, description="The status of the requirement.")
    verification_method: Optional[str] = Field(None, description="The verification method of the requirement.")
