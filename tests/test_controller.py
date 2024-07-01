import os
import unittest
from unittest.mock import patch

import mongomock
from pymongo import MongoClient
from pymongo.collection import Collection

from notion_mbse.controllers import ControllableElement
from notion_mbse.controllers import MongoCollectionController
from notion_mbse.models import Element

MONGO_URI = os.getenv("MONGO_URI")
MONGO_TEST_DB = "test_db"
MONGO_TEST_COLLECTION = "test_collection"


def check_environment():
    assert MONGO_URI is not None, "MONGO_URI is not set in the environment variables."


class TestElementManager(unittest.TestCase):
    @patch("pymongo.MongoClient", new=mongomock.MongoClient)
    def setUp(self):
        client = MongoClient(MONGO_URI)
        db = client[MONGO_TEST_DB]
        collection: Collection = db[MONGO_TEST_COLLECTION]

        self.controller = MongoCollectionController[Element](collection, Element)

        self.element = ControllableElement(
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
        self.element.use_controller(self.controller)

    def test_create(self):
        assert self.element.create()
        assert self.element.id is not None
        assert self.element.created_at is not None
        assert self.element.modified_at is None

    def test_read(self):
        assert self.element.create()
        assert self.element.read()
        assert self.element.id is not None
        assert self.element.created_at is not None
        assert self.element.modified_at is None

    def test_update(self):
        assert self.element.create()
        self.element.name = "Updated Test Element"
        assert self.element.update()
        assert self.element.id is not None
        assert self.element.created_at is not None
        # assert self.element.modified_at is not None
        assert self.element.name == "Updated Test Element"

    def tearDown(self):
        self.element.delete()
        # self.controller.close()
