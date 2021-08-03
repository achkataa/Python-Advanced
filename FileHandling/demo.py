# #
# # try:
# #     file = open("test.txt")
# #     print("test.txt opened")
# # except FileNotFoundError:
# #     print("File not found")
#
# with open("test.txt", "r") as file:
#     print(file.readline())


def create_file(name_of_file):
    with open(name_of_file, "w") as file:
        file.write("")


create_file("file.txt")