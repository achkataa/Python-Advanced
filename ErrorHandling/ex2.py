class ValueCannotBeNegativeError(Exception):
    pass

def check_if_numbers_are_positive(numbers):
    for n in numbers:
        if n < 0:
            raise ValueCannotBeNegativeError(f'{n} is a negative number')


numbers = [1, 2, -3, 4, 5]


check_if_numbers_are_positive(numbers)
print("All the numbers are positive")