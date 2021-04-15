brackets = input()

open = []

for br in brackets:
    if br == "{" or br == "[" or br == "(":
        open.append(br)
    else:
        if not open:
            print("NO")
            exit(0)
        else:
            example = open.pop() + br
            if not example == "()" and not example == "{}" and not example == "[]":
                print("NO")
                exit(0)
            else:
                continue


if open:
    print("NO")
else:
    print("YES")




