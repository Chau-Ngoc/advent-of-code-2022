from utils import extract_text_lines_from_file


def create_rows_of_trees(forest):
    rows_of_trees = []

    for row in forest:
        row_of_trees = []

        for tree in row:
            row_of_trees.append(int(tree))

        rows_of_trees.append(row_of_trees)

    return rows_of_trees


input_content = map(str.strip, extract_text_lines_from_file("input.txt"))

grid = create_rows_of_trees(input_content)

ROWS = len(grid)
COLUMNS = len(grid[0])

number_of_visible_trees = (ROWS * 2) + ((COLUMNS - 2) * 2)
max_viewing_distance = 0

for cur_row_index, row in enumerate(grid[1:-1]):
    cur_row_index += 1

    for cur_index, cur_tree in enumerate(row[1:-1]):
        cur_index += 1
        viewing_distance = 1

        left_trees = [tree for tree in row[cur_index - 1 :: -1]]
        right_trees = [tree for tree in row[cur_index + 1 :]]
        above_trees = [row[cur_index] for row in grid[cur_row_index - 1 :: -1]]
        below_trees = [row[cur_index] for row in grid[cur_row_index + 1 :]]

        # if the tallest tree from one of the directions is lower than the cur_tree
        # then cur_tree is visible from one of those directions
        if (
            max(left_trees) < cur_tree
            or max(right_trees) < cur_tree
            or max(above_trees) < cur_tree
            or max(below_trees) < cur_tree
        ):
            number_of_visible_trees += 1

        for list_of_trees in [
            left_trees,
            right_trees,
            above_trees,
            below_trees,
        ]:
            # filter for trees that are taller than or equal to the cur_tree
            te_trees = list(filter(lambda x: x >= cur_tree, list_of_trees))

            if len(te_trees) == 0:
                viewing_distance *= len(list_of_trees)
            elif len(te_trees) > 0:
                viewing_distance *= len(
                    list_of_trees[: list_of_trees.index(te_trees[0]) + 1]
                )

        if viewing_distance >= max_viewing_distance:
            max_viewing_distance = viewing_distance


print(number_of_visible_trees)
print(max_viewing_distance)
