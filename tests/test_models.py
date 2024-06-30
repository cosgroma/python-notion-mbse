from bson import ObjectId

from notion_mbse.models import Element
from notion_mbse.models import PydanticObjectId


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


# def use_controller(self, controller: BaseController):
# def to_element(self) -> Element:
# def from_element(cls, element: Element):
# def from_dict(cls, element_dict: Dict[str, Any]):
# def to_dict(self):
# def create(self):
# def update(self):
# def read(self):
# def delete(self):
# def __str__(self):
# def create_dynamic_page_class(name, fields):
# def create_db_page_from_schema(schema):
