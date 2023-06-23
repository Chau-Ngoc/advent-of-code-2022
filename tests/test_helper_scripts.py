from pathlib import Path

from helper_scripts import cwd


def test_init_files_exist():
    for child in cwd.iterdir():
        if child.match("day-*"):
            assert Path(child / "__init__.py").exists()
