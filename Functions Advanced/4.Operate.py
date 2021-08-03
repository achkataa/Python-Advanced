from functools import reduce

def operate(operator, *args):
    # if operator == "+":
    #     return sum(args)
    # elif operator == "-":
    #     return reduce(lambda x, y: x - y, args)
    # elif operator == "*":
    #     return reduce(lambda x, y: x * y, args)
    # elif operator == "/":
    #     return reduce(lambda x, y: x / y, args)
    return reduce(lambda x,y: eval(f"{x} {operator} {y}"), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
