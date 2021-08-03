import re

def count_punctuation(text):
    result = re.findall(r"[-,.!?']", text)
    return len(result)

def count_letters(text):
    result = re.findall(r"[A-Za-z]", text)
    return len(result)

with open("text.txt", "r") as file:
    lines = file.readlines()
    for count_line in range(len(lines)):
        line = lines[count_line]
        letter_count = count_letters(line)
        punctuation_count = count_punctuation(line)
        with open("output.txt", "a") as file:
            file.write(f"Line {count_line+1}: {line} ({letter_count})({punctuation_count})""\n")


