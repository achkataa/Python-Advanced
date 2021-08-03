import string

alphabet = list(string.ascii_lowercase)


rows, cols = [int(i) for i in input().split()]

matrix = []

for row_index in range(rows):
    line = [alphabet[row_index] + alphabet[row_index + col_index] + alphabet[row_index] for col_index in range(cols)]
    matrix.append(line)


for el in matrix:
    print(*el)