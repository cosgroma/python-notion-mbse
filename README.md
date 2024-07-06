# Model Based Systems Engineering using Notion DBs and Relation Columns

- Free software: MIT license
- Documentation: <https://cosgroma.github.io/python-notion-mbse>

## Development Status

| Branch | Status |
| ------ | ------ |
| GitHub Actions Build Status | [![GitHub Actions Build Status](https://github.com/cosgroma/python-notion-mbse/actions/workflows/github-actions.yml/badge.svg)](https://github.com/cosgroma/python-notion-mbse/actions) |
| Coverage Status | [![Coverage Status](https://codecov.io/gh/cosgroma/python-notion-mbse/branch/main/graphs/badge.svg?branch=main)](https://app.codecov.io/github/cosgroma/python-notion-mbse) |
| PyPI Package latest release | [![PyPI Package latest release](https://img.shields.io/pypi/v/notion-mbse.svg)](https://pypi.org/project/notion-mbse) |
| PyPI Wheel | [![PyPI Wheel](https://img.shields.io/pypi/wheel/notion-mbse.svg)](https://pypi.org/project/notion-mbse) |
| Supported versions | [![Supported versions](https://img.shields.io/pypi/pyversions/notion-mbse.svg)](https://pypi.org/project/notion-mbse) |
| Supported implementations | [![Supported implementations](https://img.shields.io/pypi/implementation/notion-mbse.svg)](https://pypi.org/project/notion-mbse) |
| Commits since latest release | [![Commits since latest release](https://img.shields.io/github/commits-since/cosgroma/python-notion-mbse/v0.0.0.svg)](https://github.com/cosgroma/python-notion-mbse/compare/v0.0.0...main) |

## Features

- **TODO**

## Installation

```bash
pip install notion-mbse
```

You can also install the in-development version with:

```bash
git clone https://github.com/cosgroma/python-notion-mbse.git
cd python-notion-mbse
python setup.py install
```

## Documentation

To use the project:

```python
import notion_mbse

```

## Development

To run all the tests run:

```bash
tox
```

Note, to combine the coverage data from all the tox environments run:

```bash
set PYTEST_ADDOPTS=--cov-append
tox
```
