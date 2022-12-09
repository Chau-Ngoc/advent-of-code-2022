from common import priorities, rucksacks

common_items = []
for rucksack in rucksacks:
    divisor = int(len(rucksack) / 2)
    for item in rucksack[:divisor]:
        if item in rucksack[divisor:]:
            common_items.append(item)
            break

priority_sum = 0
for item in common_items:
    priority_sum += priorities[item]

print(priority_sum)
