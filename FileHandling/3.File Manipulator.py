import os

command = input()


def create_file(name_of_file):
    with open(name_of_file, "w") as file:
        file.write("")

def add_content(name_of_file, text):
    with open(name_of_file, "a") as file:
        file.write(text+"\n")

def replace_strings(name_of_file, old_str, new_str):
    try:
        with open(name_of_file, "a") as file:
            for line in file:
                file.write(line.replace(old_str, new_str))
    except:
        print("An error occurred")

def delete_file(name_of_file):
    try:
        os.remove(name_of_file)
    except:
        print("An error occurred")



while command != "End":
    data = command.split("-")
    action = data[0]

    if action == "Create":
        file_name = data[1]
        create_file(file_name)

    elif action == "Add":
        file_name = data[1]
        content = data[2]
        add_content(file_name, content)

    elif action == "Replace":
        file_name = data[1]
        old_string = data[2]
        new_string = data[3]
        replace_strings(file_name, old_string, new_string)
    elif action == "Delete":
        file_name = data[1]
        delete_file(file_name)



    command = input()