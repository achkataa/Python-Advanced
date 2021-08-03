size = int(input())

matrix = []

for i in range(size):
    line = [int(r) for r in input().split(", ")]
    matrix.append(line)



#FIRST WAY
# result_ll = []
#
# result = [[result_ll.append(el) for el in line] for line in matrix]
#
# print(result_ll)

#SECOND WAY
print([x for row in matrix for x in row])






