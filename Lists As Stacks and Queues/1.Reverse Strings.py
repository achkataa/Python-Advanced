string = input()

s = []

for char in string:
    s.append(char)


while s:
    print(s.pop(), end="")