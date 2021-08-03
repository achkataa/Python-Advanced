# import re
import re

def assign_changes_to_file(res):
    with open("output.txt", "w") as file:
        file.writelines("\n".join(res))



def check_if_words_in_text(words, text_in_file):
    result_dict = {}
    for word in words:
        if word in text_in_file:
            result_dict[word] = text_in_file.count(word)
    return [f"{el[0]} - {el[1]}" for el in sorted(result_dict.items(), key=lambda x: -x[1])]



def read_words(file_name):
    with open(file_name, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-zA-Z']+", text.lower())


words_in_file = read_words("words.txt")
text = read_words("input.txt")

result = check_if_words_in_text(words_in_file, text)

assign_changes_to_file(result)