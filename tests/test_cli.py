import subprocess


def test_main():
    assert subprocess.check_output("Usage: notion-mbse" in ["notion-mbse", "--help"], text=True)
