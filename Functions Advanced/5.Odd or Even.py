command = input()
numbers = [int(num) for num in input().split()]

def print_results(nums):
    print(sum(nums) * len(numbers))


def needed_numbers(nums):
    if command == "Odd":
        nums = [num for num in nums if num % 2 != 0]
    else:
        nums = [num for num in nums if num % 2 == 0]
    print_results(nums)




needed_numbers((numbers))

