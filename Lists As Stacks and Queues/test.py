green_light = 10

string = "Mercedes"
for char in string:
    if green_light > 0:
        string = string.replace(char, "", 1)
        green_light -= 1
    else:
        break
