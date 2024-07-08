from bson import ObjectId

from notion_mbse.models import DirectedRelationship
from notion_mbse.models import Element
from notion_mbse.models import PydanticObjectId
from notion_mbse.models import RelationshipType


def test_pydantic_object_id():
    oid = PydanticObjectId()
    assert oid
    assert str(oid) == str(ObjectId(oid))
    assert str(oid) == str(ObjectId(str(oid)))


def test_element_basic():
    element = Element(
        name="Test Element",
        description="This is a test element.",
        version="1.0.0",
        tags=["test", "element"],
        type="Test",
        sub_type="Element",
        created_by="Test User",
        modified_by="Test User",
        status="Active",
        documentation="This is the documentation for the test element.",
        ref_ids=["12345", "67890"],
    )
    assert element.id
    assert element.name == "Test Element"
    assert element.description == "This is a test element."
    assert element.version == "1.0.0"
    assert element.tags == ["test", "element"]
    assert element.type == "Test"
    assert element.sub_type == "Element"
    assert element.created_by == "Test User"
    assert element.modified_by == "Test User"
    assert element.status == "Active"
    assert element.documentation == "This is the documentation for the test element."
    assert element.ref_ids == ["12345", "67890"]
    assert element.created_at
    assert element.modified_at is None

    element_dict = element.model_dump()
    assert element_dict["id"]
    assert element_dict["name"] == "Test Element"
    assert element_dict["description"] == "This is a test element."
    assert element_dict["version"] == "1.0.0"
    assert element_dict["tags"] == ["test", "element"]
    assert element_dict["type"] == "Test"
    assert element_dict["sub_type"] == "Element"
    assert element_dict["created_by"] == "Test User"
    assert element_dict["modified_by"] == "Test User"
    assert element_dict["status"] == "Active"
    assert element_dict["documentation"] == "This is the documentation for the test element."
    assert element_dict["ref_ids"] == ["12345", "67890"]
    assert element_dict["created_at"]


# def set_with_element(self, element: "Element"):


def test_element_set_with_element():
    element = Element()
    element.set_with_element(
        Element(
            name="Test Element",
            description="This is a test element.",
            version="1.0.0",
            tags=["test", "element"],
            type="Test",
            sub_type="Element",
            created_by="Test User",
            modified_by="Test User",
            status="Active",
            documentation="This is the documentation for the test element.",
            ref_ids=["12345", "67890"],
        )
    )
    assert element.id
    assert element.name == "Test Element"
    assert element.description == "This is a test element."
    assert element.version == "1.0.0"
    assert element.tags == ["test", "element"]
    assert element.type == "Test"
    assert element.sub_type == "Element"
    assert element.created_by == "Test User"
    assert element.modified_by == "Test User"
    assert element.status == "Active"
    assert element.documentation == "This is the documentation for the test element."
    assert element.ref_ids == ["12345", "67890"]
    assert element.created_at
    assert element.modified_at is None


def test_directed_relationship():
    source_element = Element(
        name="Source Element",
        description="This is the source element.",
        version="1.0.0",
        tags=["source", "test"],
        sub_type="source",
        created_by="John Doe",
        modified_by="Jane Doe",
        status="active",
        documentation="This is the documentation for the source element.",
        ref_ids=["Ref1", "Ref2"],
    )
    target_element = Element(
        name="Target Element",
        description="This is the target element.",
        version="1.0.0",
        tags=["target", "test"],
        sub_type="target",
        created_by="John Doe",
        modified_by="Jane Doe",
        status="active",
        documentation="This is the documentation for the target element.",
        ref_ids=["Ref1", "Ref2"],
    )
    relationship = DirectedRelationship(
        name="Example Relationship",
        description="This is an example relationship.",
        version="1.0.0",
        tags=["example", "test"],
        sub_type="example",
        created_by="John Doe",
        modified_by="Jane Doe",
        status="active",
        documentation="This is the documentation for the example relationship.",
        ref_ids=["Ref1", "Ref2"],
        type=RelationshipType.DEPENDENCY,
        source_element_id=source_element.id,
        target_element_id=target_element.id,
    )
    assert relationship.id
    assert relationship.name == "Example Relationship"
    assert relationship.description == "This is an example relationship."
    assert relationship.version == "1.0.0"
    assert relationship.tags == ["example", "test"]
    assert relationship.type == RelationshipType.DEPENDENCY
    assert relationship.source_element_id == source_element.id
    assert relationship.target_element_id == target_element.id
    assert relationship.created_at
    assert relationship.modified_at is None

    rev_relationship = DirectedRelationship(
        name="Example DirectedRelationship",
        description="This is an example relationship.",
        version="1.0.0",
        tags=["example", "test"],
        sub_type="example",
        created_by="John Doe",
        modified_by="Jane Doe",
        status="active",
        documentation="This is the documentation for the example relationship.",
        ref_ids=["Ref1", "Ref2"],
        type=RelationshipType.DEPENDENCY,
        source_element_id=target_element.id,
        target_element_id=source_element.id,
    )

    assert rev_relationship.id
    assert rev_relationship.name == "Example DirectedRelationship"
    assert rev_relationship.description == "This is an example relationship."
    assert rev_relationship.version == "1.0.0"
    assert rev_relationship.tags == ["example", "test"]
    assert rev_relationship.type == RelationshipType.DEPENDENCY

    assert rev_relationship.source_element_id == target_element.id
    assert rev_relationship.target_element_id == source_element.id
