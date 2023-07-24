def eval_str(line):
    try:
        return eval(line)
    except SyntaxError:
        return line


def compare(first: list | int, second: list | int):
    if type(first) == int:
        if type(second) == int:
            return first - second
        else:
            return compare([first], second)
    else:
        if type(second) == int:
            return compare(first, [second])

    for a, b in zip(first, second):
        v = compare(a, b)
        if v:
            return v

    return len(first) - len(second)
