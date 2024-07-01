from bson import ObjectId

from notion_mbse.models import Element
from notion_mbse.models import PydanticObjectId
from notion_mbse.models import Relationship
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


def test_relationship():
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
    relationship = Relationship(
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
        type=RelationshipType.ASSOCIATION,
        source_element_id=source_element.id,
        target_element_id=target_element.id,
    )
    print(relationship.model_dump())
    rev_relationship = Relationship(
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
        type=RelationshipType.ASSOCIATION,
        source_element_id=target_element.id,
        target_element_id=source_element.id,
    )
    print(rev_relationship.model_dump())
