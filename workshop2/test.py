board = [["", "", ""] for _ in range(3)]


# for col_number in range(len(board)):
#     for row_number in range(len(board)):
#         board[row_number][col_number] = N

print(board)

print()


for row_number in range(len(board)):
    board[row_number][0] = None

print(board)
