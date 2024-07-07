# Users Guide

## Command Line Interface

* Initialization Command
* Setting Up Configuration Command
* Creating Viewpoints Command
* Linking Elements Command
* Fetching Data Command
* Viewing and Navigating Command
* Synchronization Command
* Saving State Command
* Loading State Command
* Help Command
* Download Command

### Initialization Command

**Command**: `init`

**Description**: Initializes the project in the current directory. Creates necessary directories and files, including the .env file.

**Usage**: `notion-mbse init`

### Setting Up Configuration Command

**Command**: `config`

**Description**: Configures the environment settings like database IDs, API tokens, etc.

**Usage**: `notion-mbse config --set DATABASE_ID=12345 --set API_TOKEN=abcd1234`

### Creating Viewpoints Command

**Command**: `create`

**Sub-commands**:

- `viewpoint`: Creates a new viewpoint.
- `element`: Creates a new UAF element.

**Usage**:

- `notion-mbse create viewpoint --name "Strategic"`
- `notion-mbse create element --name "System A" --type "System"`

### Linking Elements Command

**Command**: `link`

**Description**: Establishes relationships between UAF elements.

**Usage**: `notion-mbse link --source "System A" --target "Process B" --relation "depends_on"`

### Fetching Data Command

**Command**: `fetch`

**Description**: Fetches and updates local data from Notion.

**Usage**: `notion-mbse fetch --elements`

### Viewing and Navigating Command

**Command**: `view`

**Sub-commands**:

- `viewpoint`: Displays details of a viewpoint.
- `element`: Displays details of an element.

**Usage**:

- `notion-mbse view viewpoint --name "Strategic"`
- `notion-mbse view element --name "System A"`

### Synchronization Command

**Command**: `sync`

**Description**: Synchronizes local changes with the Notion database.

**Usage**: `notion-mbse sync`

### Saving State Command

**Command**: `save`

**Description**: Saves the current state of the project, which can be useful for checkpoints.

**Usage**: `notion-mbse save --state "checkpoint1"`

### Loading State Command

**Command**: `load`

**Description**: Loads a previously saved state.

**Usage**: `notion-mbse load --state "checkpoint1"`

### Help Command

**Command**: `help`

**Description**: Displays help information for commands.

**Usage**: `notion-mbse help [command]`

## Download Command

**Command**: `download`

**Usage**:

::: mkdocs-click
    :module: notion_mbse.ui.cli
    :command: download
