from common import input_content, pattern, stacks

for line in input_content:
    match = pattern.match(line)
    (amount, from_, to) = match.groups()

    for i in range(int(amount)):
        last = stacks[int(from_) - 1].pop()
        stacks[int(to) - 1].append(last)

top_creates = ""
for stack in stacks:
    last = stack[-1]
    top_creates += last

print(top_creates)
