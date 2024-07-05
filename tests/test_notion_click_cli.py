from click.testing import CliRunner

from notion_mbse.ui.cli import cli


def test_download_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["download", "https://example.com", "-t", "pdf", "-d", "downloads"])
    assert "Downloading from https://example.com as pdf to downloads" in result.output
    assert result.exit_code == 0
