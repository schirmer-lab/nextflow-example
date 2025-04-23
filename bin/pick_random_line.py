#! /usr/bin/env python

import random
import re
import sys


def pick_random_line(cleaned_script_path: str, output_path: str, min_word_count) -> None:
    with open(cleaned_script_path, 'r') as cleaned_script:
        all_lines = cleaned_script.readlines()

    # pick radnom line
    while True:
        line_index = random.randint(0, len(all_lines))
        if all_lines[line_index] != "--" and ':' in all_lines[line_index]:
            break
    # check if previous line contains ? or this line includes yes or no
    line_to_return = all_lines[line_index]
    if include_previous_line(all_lines, line_index):
        line_to_return = f"{all_lines[line_index-1]}{line_to_return}"
    # check if the next line should be included
    if include_previous_line(all_lines, line_index+1):
        line_to_return = f"{line_to_return}{all_lines[line_index+1]}"
        line_index += 1

    while line_index+1 < len(all_lines) and (not all_lines[line_index+1].startswith("--")) and word_count(line_to_return) <= min_word_count:
        line_index += 1
        line_to_return += all_lines[line_index]

    with open(output_path, "w") as output:
        output.write(line_to_return)


def word_count(line: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", line))


def include_previous_line(all_lines: list, line_index: int) -> bool:
    if line_index == 0 or all_lines[line_index-1].startswith("--") or all_lines[line_index].startswith("--"):
        return False
    return bool(re.search(r'\b(yes|no)\b', all_lines[line_index], flags=re.IGNORECASE)) or '?' in all_lines[line_index-1]


if __name__ == "__main__":
    pick_random_line(sys.argv[1], sys.argv[2], int(sys.argv[3]))
