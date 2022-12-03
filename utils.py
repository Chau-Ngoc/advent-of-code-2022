import numpy as np


def extract_text_lines_from_file(filepath):
    with open(filepath, "r") as f:
        return f.readlines()


def str_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None


def str_to_nan(value):
    try:
        return int(value)
    except ValueError:
        return np.nan
