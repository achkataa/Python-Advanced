numbers = [int(num) for num in input().split()]

def print_results(min, max, sum):
    print(f"The minimum number is {min}")
    print(f"The maximum number is {max}")
    print(f"The sum number is: {sum}")

def find_min_max_sum(nums):
    min_num = min(nums)
    max_num = max(nums)
    sum_list = sum(nums)
    print_results(min_num, max_num, sum_list)



find_min_max_sum((numbers))




