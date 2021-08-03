# try:
#     number = int(input())
#     print(number + 1)
# except:
#     print("Not a number")


def print_calculate():
    try:
        number = int(input())
        print(number + 1)
    except ValueError:
        print("Not a number")



print_calculate()



