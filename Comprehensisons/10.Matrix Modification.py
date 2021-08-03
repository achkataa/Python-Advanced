size = int(input())

matrix = []

for i in range(size):
    line = [int(r) for r in input().split()]
    matrix.append(line)

for index in range(size):
    command = input()
    if not command == "END":
        command = command.split()
        action = command[0]
        row = int(command[1])
        col = int(command[2])
        value = int(command[3])

        if size > row > -1 and size > col > -1:
            if action == "Add":
                matrix[row][col] += value
            else:
                matrix[row][col] -= value

        else:
            print("Invalid coordinates")
    else:
        break


matrix = [print(*line) for line in matrix]



