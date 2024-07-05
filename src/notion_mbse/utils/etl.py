# Python script that implements extract, transform, and load (ETL) operations for Notion databases.
# it uses the NotionDatabase class from the databasetools package to interact with Notion databases.
# has function that takes the excel file, sheet name and Pydantic Model name as arguments.
# and convert them to a pandas DataFrame, does column mapping if nessesary,
# and then upload the data to a Notion database.

# downloads NotionDatabase data by converting it to a pandas DataFrame and saving it as a CSV file or Excel file.
# can separatly download the notion database global properties as json file.

# from pymongo import MongoClient
import os

import dotenv

# from pydantic.schema import schema
from notion_mbse.models import Element
from notion_mbse.models import create_db_page_from_schema

dotenv.load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")
NOTION_OMG_SPEC_DB_URL = os.getenv("NOTION_OMG_SPEC_DB_URL")
NOTION_MBSE_ROOT_URL = os.getenv("NOTION_MBSE_ROOT_URL")

## Data Models


def test_schema_to_notion():
    element_schema = Element.model_json_schema()
    NotionElement = create_db_page_from_schema(element_schema)
    assert NotionElement.name.field == "Name"
    assert NotionElement.description.field == "Description"
    assert NotionElement.version.field == "Version"
