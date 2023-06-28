from argparse import Action

from constants import BASEDIR


class NextPackageAction(Action):
    def __init__(self, option_strings, dest, *args, **kwargs):
        super().__init__(option_strings, dest, *args, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        for value in values:
            new_dir = BASEDIR / f"day-{value}"
            init_file = new_dir / "__init__.py"

            new_dir.mkdir()
            init_file.touch(exist_ok=False)
