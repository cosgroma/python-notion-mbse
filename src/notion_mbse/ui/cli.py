"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mnotion_mbse` python will execute
    ``__main__.py`` as a script. That means there will not be any
    ``notion_mbse.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there"s no ``notion_mbse.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""

import click

# from ..core import compute


# Decorator for common options
def common_options(f):
    f = click.option("-t", "--type", default="command specific", help="The type of operation [default: command specific].")(f)
    f = click.option("-k", "--key", default="NOTION_API_KEY", help="The Notion API key [default: NOTION_API_KEY].")(f)
    f = click.option("-d", "--dir", type=click.Path(), help="The directory to save files [default: ./].")(f)
    f = click.option("--verbose", is_flag=True, help="Produce verbose output.")(f)
    f = click.option("--quiet", is_flag=True, help="Minimize output.")(f)
    return f


@click.group()
def cli():
    """A CLI tool for interacting with Notion."""


@cli.command()
@common_options
@click.argument("url")
def download(url, type, key, dir, verbose, quiet):
    """Download files from Notion."""
    click.echo(f"Downloading from {url} as {type} to {dir} using key {key}")


@cli.command()
@common_options
@click.argument("url")
@click.option("-f", "--file", default=None, type=click.Path())
@click.option("-s", "--sheet", default="Sheet1", help="The sheet name for Excel exports.")
@click.option("--overwrite", is_flag=True, help="Overwrite the existing file if it exists.")
@click.option("--append", is_flag=True, help="Append to the existing file if it exists.")
@click.option("-m", "--mapping", type=click.File("r"), help="The column mapping for xlsx exports.")
@click.option("--extend-columns", is_flag=True, help="Extend the existing columns when new data is appended.")
@click.option("--target-columns", is_flag=True, help="Adjust the target columns to match the specified mapping.")
def export(url, type, dir, file, sheet, overwrite, append, mapping, extend_columns, target_columns):
    """Export a Notion database or page."""
    click.echo(f"Exporting {url} as {type}")
    if dir:
        click.echo(f"Saving to directory: {dir}")
    if file:
        click.echo(f"Saving to file: {file}")
    if mapping:
        click.echo(f"Using column mapping: {mapping.read()}")


if __name__ == "__main__":
    cli()
