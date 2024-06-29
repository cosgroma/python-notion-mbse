========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |github-actions| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|

.. |github-actions| image:: https://github.com/cosgroma/python-notion-mbse/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/cosgroma/python-notion-mbse/actions

.. |codecov| image:: https://codecov.io/gh/cosgroma/python-notion-mbse/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/cosgroma/python-notion-mbse

.. |version| image:: https://img.shields.io/pypi/v/notion-mbse.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/notion-mbse

.. |wheel| image:: https://img.shields.io/pypi/wheel/notion-mbse.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/notion-mbse

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/notion-mbse.svg
    :alt: Supported versions
    :target: https://pypi.org/project/notion-mbse

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/notion-mbse.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/notion-mbse

.. |commits-since| image:: https://img.shields.io/github/commits-since/cosgroma/python-notion-mbse/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/cosgroma/python-notion-mbse/compare/v0.0.0...main



.. end-badges

Model Based Systems Engineering using Notion DBs and Relation Columns

* Free software: MIT license

Installation
============

::

    pip install notion-mbse

You can also install the in-development version with::

    pip install https://github.com/cosgroma/python-notion-mbse/archive/main.zip


Documentation
=============


To use the project:

.. code-block:: python

    import notion_mbse
    notion_mbse.compute(...)



Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
