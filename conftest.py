import pathlib

import pytest


@pytest.fixture
def resources_dir():
    cwd = pathlib.Path(__file__).parent
    return cwd / "tests" / "resources"
