start = int(input())
end = int(input())


#FIRST WAY
# result = [i for i in range(start, end + 1) if i % 2 == 0 or i % 3 == 0 or i % 4 == 0 or i % 5 == 0 or i % 6 == 0 or i % 7 == 0 or i % 8 == 0 or i % 9 == 0 or i % 10 == 0]
# print(result)

#SECOND WAY

def is_valid(x):
    return any(x % i == 0 for i in range(2, 11))

result = [x for x in range(start, end + 1) if is_valid(x)]
print(result)

