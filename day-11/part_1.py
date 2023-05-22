from common import monkeys, throw_to

for i in range(20):
    for monkey in monkeys:
        items = monkey.items.copy()
        for index, item in enumerate(items):
            worry_level = monkey.inspect(item) // 3
            item_index = monkey.items.index(item)
            monkey.items[item_index] = worry_level

            choice = monkey.test(worry_level)
            throw_to(
                monkey,
                monkeys[monkey.true_monkey],
                monkeys[monkey.false_monkey],
                choice,
                item_index,
            )

inspection_counts = []
for monkey in monkeys:
    inspection_counts.append(monkey.inspection_count)

inspection_counts.sort()
print(inspection_counts[-1] * inspection_counts[-2])
