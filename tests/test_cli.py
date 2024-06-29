import subprocess


def test_main():
    assert subprocess.check_output(["notion-mbse", "foo", "foobar"], text=True) == "foobar\n"
