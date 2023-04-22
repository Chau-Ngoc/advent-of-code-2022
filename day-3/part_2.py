from common import ElvesGroup, priorities, rucksacks

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
