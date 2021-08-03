from math import floor
size = int(input())

matrix = []
p_row = None
p_col = None

path = []

points = 0

for i in range(size):
    line = [l for l in input().split()]
    matrix.append(line)
    if "P" in line:
        p_row = i
        p_col = line.index("P")


def check_if_index_is_valid(matrix, p_row, p_col):
    if p_row >= 0 and p_row < len(matrix) and p_col >= 0 and p_col < len(matrix):
        return True
    return False



def game_over(points):
    points = floor(points * 0.5)
    print(f"Game over! You've collected {points} coins.")

def add_path(row, col):
    path.append([row, col])

while True:
    command = input()

    if command == "up":
        if check_if_index_is_valid(matrix, p_row - 1, p_col):
            p_row -= 1
            if matrix[p_row][p_col] != "X":
                points += int(matrix[p_row][p_col])
                add_path(p_row, p_col)
            else:
                game_over(points)
                break
        else:
            game_over(points)
            break

    elif command == "down":
        if check_if_index_is_valid(matrix, p_row + 1, p_col):
            p_row += 1
            if matrix[p_row][p_col] != "X":
                points += int(matrix[p_row][p_col])
                add_path(p_row, p_col)
            else:
                game_over(points)
                break
        else:
            game_over(points)
            break
    elif command == "left":
        if check_if_index_is_valid(matrix, p_row, p_col - 1):
            p_col -= 1
            if matrix[p_row][p_col] != "X":
                points += int(matrix[p_row][p_col])
                add_path(p_row, p_col)
            else:
                game_over(points)
                break
        else:
            game_over(points)
            break

    elif command == "right":
        if check_if_index_is_valid(matrix, p_row, p_col + 1):
            p_col += 1
            if matrix[p_row][p_col] != "X":
                points += int(matrix[p_row][p_col])
                add_path(p_row, p_col)
            else:
                game_over(points)
                break
        else:
            game_over(points)
            break

    if points >= 100:
        print(f"You won! You've collected {points} coins.")
        break

print("Your path: ")
for row in path:
    print(row)

