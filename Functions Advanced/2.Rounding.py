numbers = list(map(float, input().split()))

def round_numbers(nums):
    return list(map(lambda x: round(x), nums))


print(round_numbers(numbers))