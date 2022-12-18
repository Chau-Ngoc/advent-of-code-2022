from common import input_content, pattern, stacks

for line in input_content:
    match = pattern.match(line)
    (amount, from_, to) = tuple(map(int, match.groups()))

    selected_crates = stacks[from_ - 1][-amount:]
    stacks[from_ - 1] = stacks[from_ - 1][:-amount]
    stacks[to - 1].extend(selected_crates)

top_creates = ""
for stack in stacks:
    last = stack[-1]
    top_creates += last

print(top_creates)
