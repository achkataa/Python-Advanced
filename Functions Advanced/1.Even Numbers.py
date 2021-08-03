numbers = [int(num) for num in input().split()]


result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)