import textwrap
from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter

import action_classes as act_clss

arg_parser = ArgumentParser(
    prog="Advent Of Code 2022 helper scripts",
    description=textwrap.dedent(
        """
    This helps you with your journey through advent of code
    -------------------------------------------------------
    """
    ),
    epilog="Enjoy coding",
    formatter_class=RawDescriptionHelpFormatter,
)

arg_parser.add_argument(
    "--next-package",
    help=(
        "Create a new python package whose name follows 'day-%(metavar)s'"
        " pattern (e.g. day-11)"
    ),
    type=int,
    metavar="NUM",
    dest="day_num",
    action=act_clss.NextPackageAction,
    nargs="+",
)
arguments: Namespace = arg_parser.parse_args()
