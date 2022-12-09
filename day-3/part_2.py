import re

from common import priorities, rucksacks


class ElvesGroup:
    pattern = re.compile(r"(\w+),(\w+),(\w+)")

    def __init__(self, rucksacks: str):
        self.rucksacks = rucksacks

    def find_badge(self):
        match = self.pattern.match(self.rucksacks)
        groups = match.groups()

        for item in groups[0]:
            if item in groups[1] and item in groups[2]:
                return item


counter = 0
group_rucksacks = ""
priority = 0

for rs in rucksacks:
    group_rucksacks += f"{rs},"

    if counter == 2:
        group = ElvesGroup(group_rucksacks)
        group_badge = group.find_badge()
        priority += priorities[group_badge]

        counter = 0
        group_rucksacks = ""

        continue

    counter += 1

print(priority)
