import numpy as np
import pytest

from utils import extract_text_lines_from_file, str_to_int, str_to_nan


def test_extract_text_lines_from_file(resources_dir):
    file_path = resources_dir / "test_input.txt"
    expected = ["line 1\n", "line 2\n", "line 3\n"]

    content = extract_text_lines_from_file(file_path)

    assert list(content) == expected


@pytest.mark.parametrize(
    "test_input, expected", [("123", 123), ("1", 1), ("0", 0)]
)
def test_str_to_int(test_input, expected):
    result = str_to_int(test_input)
    assert result == expected


@pytest.mark.parametrize(
    "test_input, expected", [("123", 123), ("1", 1), ("0", 0)]
)
def test_str_to_nan(test_input, expected):
    result = str_to_nan(test_input)
    assert result == expected


def test_str_to_int_return_none():
    result = str_to_int("abc")
    assert result is None


def test_str_to_nan_return_nan():
    result = str_to_nan("abc")
    assert result is np.nan
