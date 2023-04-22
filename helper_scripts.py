import pathlib

cwd = pathlib.Path(__file__).parent

for child in cwd.iterdir():
    if child.match("day-*"):
        init_file = child / "__init__.py"

        try:
            init_file.touch(exist_ok=False)
        except FileExistsError:
            continue
