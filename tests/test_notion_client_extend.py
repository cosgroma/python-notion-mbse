import os

import pytest

# from pydantic.schema import schema
from notion_mbse.utils.notion_client_extend import NotionClient
from notion_mbse.utils.notion_utils import extract_id_from_notion_url

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_OMG_SPEC_DB_URL = os.getenv("NOTION_OMG_SPEC_DB_URL")
NOTION_MBSE_ROOT_URL = os.getenv("NOTION_MBSE_ROOT_URL")


@pytest.fixture
def notion_client():
    if NOTION_API_KEY is None:
        raise ValueError("NOTION_API_KEY is not set")
    return NotionClient(token=NOTION_API_KEY)


def test_get_metadata(notion_client):
    if NOTION_MBSE_ROOT_URL is None:
        raise ValueError("NOTION_MBSE_ROOT_URL is not set")
    page_id = extract_id_from_notion_url(NOTION_MBSE_ROOT_URL)
    metadata = notion_client.get_metadata(page_id)
    assert isinstance(metadata, dict)
    assert "id" in metadata
    assert "last_edited_time" in metadata


def test_get_recent_pages(notion_client):
    recent_pages = notion_client.get_recent_pages()
    assert isinstance(recent_pages, list)
    for page in recent_pages:
        assert isinstance(page, dict)
        assert "id" in page
        assert "last_edited_time" in page


def _test_get_recent_blocks(notion_client):
    recent_blocks = notion_client.get_recent_blocks()
    assert isinstance(recent_blocks, list)
    for block in recent_blocks:
        assert isinstance(block, dict)
        assert "id" in block
        assert "last_edited_time" in block


def _test_get_blocks(notion_client):
    block_id = "your-block-id"
    blocks = notion_client.get_blocks(block_id)
    assert isinstance(blocks, list)
    for block in blocks:
        assert isinstance(block, dict)
        assert "id" in block
        assert "last_edited_time" in block


def test_get_database(notion_client):
    if NOTION_OMG_SPEC_DB_URL is None:
        raise ValueError("NOTION_OMG_SPEC_DB_URL is not set")
    database_id = extract_id_from_notion_url(NOTION_OMG_SPEC_DB_URL)
    database = notion_client.get_database(database_id)
    assert isinstance(database, list)
    for page in database:
        assert isinstance(page, dict)
        assert "id" in page
        assert "last_edited_time" in page


def test_download_url(notion_client):
    url = NOTION_MBSE_ROOT_URL
    out_dir = "./json"
    notion_client.download_url(url, out_dir)
    # Add assertions for the downloaded file


def test_download_page(notion_client):
    page_id = extract_id_from_notion_url(NOTION_MBSE_ROOT_URL)
    out_path = "./json/page.json"
    notion_client.download_page(page_id, out_path)
    # Add assertions for the downloaded file


def test_download_database(notion_client):
    database_id = extract_id_from_notion_url(NOTION_OMG_SPEC_DB_URL)
    out_dir = "./json"
    notion_client.download_database(database_id, out_dir)
    # Add assertions for the downloaded files
