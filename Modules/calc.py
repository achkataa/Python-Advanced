from calc_operations import app_add, app_subtract, app_multiply, app_divide, app_power
command = input().split()
first_num = float(command[0])
sign = command[1]
second_num = int(command[2])

mapper = {

    "+": app_add,
    "-": app_subtract,
    "*": app_multiply,
    "/": app_divide,
    "^": app_power
}

print(mapper[sign](first_num, second_num))

