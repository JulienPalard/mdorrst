import os
from pathlib import Path
import sys

import pytest

import mdorrst

FIXTURE_DIR = Path(__file__).resolve().parent / "readmes"


@pytest.mark.parametrize(
    "readme_file,readme_style",
    [
        (readme_file, readme_file.name.split(".")[-1])
        for readme_file in FIXTURE_DIR.glob("*/*/README.*")
    ],
)
def test_files(readme_file, readme_style):
    with open(readme_file, encoding="UTF-8") as readme:
        assert mdorrst.sniff(readme.read()) == readme_style


def test_main(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["mdorrst"])
    with pytest.raises(SystemExit):
        mdorrst.run()
    captured = capsys.readouterr()
    assert "--verbose" in captured.err


def test_main_on_our_readme(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["mdorrst", "README.md"])
    mdorrst.run()
    captured = capsys.readouterr()
    assert captured.out == "md\n"


def test_verbose_main_on_our_readme(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["mdorrst", "--verbose", "README.md"])
    mdorrst.run()
    captured = capsys.readouterr()
    assert "Markdown points:" in captured.out
