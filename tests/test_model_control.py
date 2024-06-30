from notion_mbse.models import ControllableElement
from notion_mbse.models import Element


def test_controlable_element_basic():
    element = ControllableElement(
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


def test_controlable_element_to_element():
    element = ControllableElement(
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
    element_dict = element.to_element().model_dump()
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


def test_controlable_element_from_element():
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
    controlable_element = ControllableElement.from_element(element)
    assert controlable_element.name == "Test Element"
    assert controlable_element.description == "This is a test element."
    assert controlable_element.version == "1.0.0"
    assert controlable_element.tags == ["test", "element"]
    assert controlable_element.type == "Test"
    assert controlable_element.sub_type == "Element"
    assert controlable_element.created_by == "Test User"
    assert controlable_element.modified_by == "Test User"
    assert controlable_element.status == "Active"
    assert controlable_element.documentation == "This is the documentation for the test element."
    assert controlable_element.ref_ids == ["12345", "67890"]
    assert controlable_element.created_at
    assert controlable_element.modified_at is None


def test_controlable_element_from_dict():
    element_dict = {
        "name": "Test Element",
        "description": "This is a test element.",
        "version": "1.0.0",
        "tags": ["test", "element"],
        "type": "Test",
        "sub_type": "Element",
        "created_by": "Test User",
        "modified_by": "Test User",
        "status": "Active",
        "documentation": "This is the documentation for the test element.",
        "ref_ids": ["12345", "67890"],
    }
    controlable_element = ControllableElement.from_dict(element_dict)
    assert controlable_element.name == "Test Element"
    assert controlable_element.description == "This is a test element."
    assert controlable_element.version == "1.0.0"
    assert controlable_element.tags == ["test", "element"]
    assert controlable_element.type == "Test"
    assert controlable_element.sub_type == "Element"
    assert controlable_element.created_by == "Test User"
    assert controlable_element.modified_by == "Test User"
    assert controlable_element.status == "Active"
    assert controlable_element.documentation == "This is the documentation for the test element."
    assert controlable_element.ref_ids == ["12345", "67890"]
    assert controlable_element.created_at
    assert controlable_element.modified_at is None


def test_controlable_element_to_dict():
    element = ControllableElement(
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
    element_dict = element.to_dict()
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
    assert element_dict["modified_at"] is None
