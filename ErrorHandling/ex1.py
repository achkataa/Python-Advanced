numbers_list = [int(num) for num in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    try:
        number = numbers_list[i]
    except:
        break
    if number <= 5:
        result *= number
    elif number > 5:
        result /= number

print(result)
