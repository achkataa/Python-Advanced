size = int(input())

matrix = []

for i in range(size):
    line = [int(r) for r in input().split(", ")]
    matrix.append(line)


result = [[num for num in line if num % 2 == 0] for line in matrix]
print(result)