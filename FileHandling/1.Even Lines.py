import re

def replace_symbols(line):
    result = re.sub(r"[-,.!?]", "@", line)
    return result.split()

with open("text.txt", "r") as file:
    lines = file.readlines()
    for line_count in range(len(lines)):
        if line_count % 2 == 0:
            print(' '.join(replace_symbols(lines[line_count])[::-1]))

