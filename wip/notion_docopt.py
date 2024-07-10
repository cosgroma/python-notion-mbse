"""Usage:
  notion.py [-hvq] download <URL> [-t <type>] [-d <dir>] [-k <key>]
  notion.py [-hvq] export <URL> [-t <type>] [-d <dir> | -f <outfile>] [--overwrite | --append] 
  notion.py [-hvq] export <URL> [-t xlsx] [-d <dir> | -f <outfile>] [-s <sheet_name>] [--overwrite | --append] [-m <column_mapping>] [--extend-columns | --target-columns]

Commands:
  download    Download files from Notion.
  export      Export a Notion database.

Arguments:
  URL         The Notion URL to process.

Options:
  -h --help           Show this screen.
  -v --verbose        Show verbose output.
  -q --quiet          Show minimal output.
  -k --key            The Notion API key [default: NOTION_API_KEY].
  -d --dir            The directory to save files [default: ./].
  -t --type           The type of operation [default: command specific].
  -f --file           The output file [default: output.<type>].
  -s --sheet          The sheet name (for xlsx export) [default: Sheet1].
  -o --overwrite      Overwrite the existing file.
  -a --append         Append to the existing file.
  -m --mapping        The column mapping for xlsx [default: None].
  --extend-columns    Extend the existing columns when new data is appended (for xlsx export).
  --target-columns    Adjust the target columns to match the specified mapping (for xlsx export).
"""

# This script is used to download files from Notion using databasetools
# This script will use docopt to parse the command line arguments
# The command line arguments are:

# This script is used to download files from Notion using databasetools
# This script will use docopt to parse the command line arguments


# Define docstring

import urllib.request
# urllib.request.urlretrieve("http://www.example.com/songs/mp3.mp3", "mp3.mp3")
from docopt import docopt
import os
from databasetools import NotionBlock
from databasetools import NotionClient
from databasetools import NotionDatabase
from databasetools import NotionPage
from databasetools.adapters.notion import utils
import pandas as pd

# Example
# def test_notion_page():
#     # page_id = extract_id_from_notion_url(TEST_PLANNING_PAGE_URL)
#     # page_id = NotionPage.get_page_id_from_url(url=TEST_PLANNING_PAGE_URL)
#     int_page = NotionPage(token=NOTION_API_KEY, page_id=PAGE_ID)
#     page, page_results = int_page.get_page()
#     page_id_no_dash = page.id.replace("-", "")
#     assert PAGE_ID == page_id_no_dash
#     # assert page.properties
#     blocks = int_page.get_blocks()
#     child_pages = int_page.get_child_pages()
#     # for child_page in child_pages:
#     #     if "test_page" in child_page.title:
#     #         print(f"deleting {child_page.title}")
#     #         child_page.delete_page()
#     test_page = int_page.add_page(title=f"test_page {datetime.now(tz=pytz.utc)}")

from pprint import pprint
from pathlib import Path

def download_file(url: str, dir: str, filename: str):
    urllib.request.urlretrieve(url, Path(dir) / filename)

def cmd_download(url: str, key: str, dir: str) -> NotionPage:
    # Get the page id from the URL
    page_id = utils.extract_id_from_notion_url(url)
    # Create a NotionPage object
    page = NotionPage(token=key, page_id=page_id)
    # Get the page content
    page_content, _ = page.get_page()
    
    # Get the blocks from the page content
    blocks = page.get_blocks()
    # Create a directory to save the files
    os.makedirs(dir, exist_ok=True)
    # Download the files from the blocks
    for block in blocks:
        if block["type"] == "file":
            pprint(block["file"])
            # {'caption': [],
            # 'file': {'expiry_time': '2024-07-05T00:28:10.945Z',
            # 'url': 'https://prod-files-secure.s3.us-west-2.amazonaws.com/376276ab-3e70-4885-9041-173598dff1e8/dccf49f3-55a5-4d8c-a940-c0172c73b8d2/Untitled.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240704T232811Z&X-Amz-Expires=3600&X-Amz-Signature=f30b8bddf76bb5b1a8cfccc48db24487eb2adc855b9a7d8f98466a452e47e7b1&X-Amz-SignedHeaders=host&x-id=GetObject'},
            # 'name': 'Untitled.txt',
            # 'type': 'file'}
            filename = block["file"]["name"]
            if "Untitled" in filename:
                filename = filename.replace("Untitled", block["id"])
            
            download_file(block["file"]["file"]["url"], dir, filename)             
        
    # print("Files downloaded successfully")

def is_url(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")


# Create, write to and save a workbook:

# df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
#                    index=['row 1', 'row 2'],
#                    columns=['col 1', 'col 2'])
# df1.to_excel("output.xlsx")  
# To specify the sheet name:

# df1.to_excel("output.xlsx",
#              sheet_name='Sheet_name_1')  
# If you wish to write to more than one sheet in the workbook, it is necessary to specify an ExcelWriter object:

# df2 = df1.copy()
# with pd.ExcelWriter('output.xlsx') as writer:  
#     df1.to_excel(writer, sheet_name='Sheet_name_1')
#     df2.to_excel(writer, sheet_name='Sheet_name_2')
# ExcelWriter can also be used to append to an existing Excel file:

# with pd.ExcelWriter('output.xlsx',
#                     mode='a') as writer:  
#     df1.to_excel(writer, sheet_name='Sheet_name_3')


def main():
    arguments = docopt(__doc__)
    # {'--dir': False,
    # '--help': False,
    # '--key': False,
    # '--quiet': False,
    # '--verbose': False,
    # '<dir>': None,
    # '<key>': None,
    # 'URL': 'https://www.notion.so/cosgroma/dbs-36166cf3565d49af87a4df42a4615a34?pvs=4',
    # 'download': True}
    if arguments["download"]:
        url = arguments["URL"]
        if not url:
            print("Please provide a Notion URL")
        if not is_url(url):
            print("Please provide a valid URL")
        key = arguments.get("--key")
        if not key:
            key = os.getenv("NOTION_API_KEY")
        
        if not key:
            print("Please provide a Notion API key")
        
        if arguments["--dir"]:
            dir = arguments.get("<dir>")
        else:
            dir = "./"
        
        cmd_download(url, key, dir)

from pprint import pprint
def test_main_args():
    arguments = docopt(__doc__)
    pprint(arguments)
    # assert arguments["URL"] == "https://www.notion.so/cosgroma/dbs-36166cf3565d49af87a4df42a4615a34?pvs=4"
    # assert arguments["download"] == True
    # assert arguments["export"] == False
    # assert arguments["help"] == False
    # assert arguments["--dir"] == False
    # assert arguments["--key"] == False
    # assert arguments["--quiet"] == False
    # assert arguments["--verbose"] == False
    # assert arguments["<dir>"] == None
    # assert arguments["<key>"] == None
if __name__ == '__main__':
    test_main_args()