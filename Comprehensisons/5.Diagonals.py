size = int(input())

matrix = []

for i in range(size):
    line = [int(r) for r in input().split(", ")]
    matrix.append(line)

def ints_into_strings(ll):
    return ", ".join(str(el) for el in ll)

first_diagonal = [matrix[i][i] for i in range(size)]
print(f"First diagonal: {ints_into_strings(first_diagonal)}. Sum: {sum(first_diagonal)}")

second_diagonal = [matrix[i][size - i - 1] for i in range(size)]
print(f"Second diagonal: {ints_into_strings(second_diagonal)}. Sum: {sum(second_diagonal)}")


