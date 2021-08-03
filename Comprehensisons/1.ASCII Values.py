letters = [i for i in input().split(", ")]

ascii_dict = {let: ord(let) for let in letters}

print(ascii_dict)