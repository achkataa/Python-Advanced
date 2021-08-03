# from functools import reduce

def app_add(num1, num2):
    return num1 + num2
    # return reduce(lambda x, y: x + y, args)

def app_subtract(num1, num2):
    return num1 - num2
    # return reduce(lambda x, y: x-y, args)

def app_multiply(num1, num2):
    return num1 * num2
    # return reduce(lambda x, y: x*y, args)

def app_divide(num1, num2):
    return num1 / num2
    # return reduce(lambda x, y: x / y, args)

def app_power(num1, num2):
    return num1 ** num2
