from utils import extract_text_lines_from_file


def find_char_position(chars, target):
    for index, char in enumerate(chars):
        if char == target:
            return index


def main(buffer, expected_length):
    result = ""

    for index, char in enumerate(buffer[0]):
        if char in result:
            char_location = find_char_position(result, char)
            result = result[char_location + 1 :]
            result += char
            continue

        result += char

        if len(result) == expected_length:
            print(index + 1)
            break


input_content = extract_text_lines_from_file("input.txt")

main(input_content, 4)
