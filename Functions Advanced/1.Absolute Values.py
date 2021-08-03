numbers = [float(i) for i in input().split()]

def convert_to_absolute_values(nums):
    # return list(map(abs, nums))
    # return [abs(n) for n in nums]
    return list(map(lambda x: abs(x), nums))

print(convert_to_absolute_values(numbers))


