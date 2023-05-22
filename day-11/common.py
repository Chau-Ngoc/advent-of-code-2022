import operator
import re
from pathlib import Path
from typing import Callable

import numpy as np

from utils import extract_text_lines_from_file


class Monkey:
    def __init__(
        self,
        items: list,
        op_fn: Callable[[int], int],
        test_fn: Callable[[int], bool],
        true_monkey: int,
        false_monkey: int,
    ):
        self.items = items
        self.op_fn = op_fn
        self.test_fn = test_fn
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspection_count = 0

    def inspect(self, value: int) -> int:
        self.inspection_count += 1
        return self.op_fn(value)

    def test(self, value: int) -> bool:
        return self.test_fn(value)

    def throw(self, index: int, monkey: "Monkey"):
        item = self.items.pop(index)
        monkey.items.append(item)

    def __repr__(self):
        return f"Monkey"


def operation(ops: list):
    ops_lookup = {"+": operator.add, "*": operator.mul}
    _, op, right = ops

    def operate(value: int) -> int:
        if right == "old":
            return ops_lookup[op](value, value)
        else:
            return ops_lookup[op](value, int(right))

    return operate


def divisible_by(by: int):
    def fn(value: int) -> bool:
        return value % by == 0

    return fn


def throw_to(monkey, to_true, to_false, choice, index):
    if choice is True:
        monkey.throw(index, to_true)
    elif choice is False:
        monkey.throw(index, to_false)


items_pattern = re.compile(r"\s{2}Starting items: (?P<items>[\d,\s]*)\s*")
op_expr_pattern = re.compile(r"\s{2}Operation: new = (?P<expr>\w+ [+*] \w+)\s*")
test_expr_pattern = re.compile(r"\s{2}Test: divisible by (?P<div_by>\d+)\s*")
if_true_pattern = re.compile(r".+true.+throw to monkey (?P<if_true>\d+)\s*")
if_false_pattern = re.compile(r".+false.+throw to monkey (?P<if_false>\d+)\s*")

input_file = Path(__file__).parent / "input.txt"
input_content = list(extract_text_lines_from_file(input_file))
number_of_newlines = input_content.count("\n")

monkey_parts = np.array_split(input_content, number_of_newlines + 1)

common_denominator = 1

monkeys = []
for monkey_part in monkey_parts:
    items = list(
        map(
            int,
            items_pattern.match(monkey_part[1])["items"].strip().split(", "),
        )
    )
    ops = op_expr_pattern.match(monkey_part[2])["expr"].split(" ")
    div_by = int(test_expr_pattern.match(monkey_part[3])["div_by"])
    if_true = int(if_true_pattern.match(monkey_part[4])["if_true"])
    if_false = int(if_false_pattern.match(monkey_part[5])["if_false"])

    common_denominator *= div_by

    op_fn = operation(ops)
    test_fn = divisible_by(div_by)

    monkeys.append(Monkey(items, op_fn, test_fn, if_true, if_false))
