my_dict = {name: ([], []) for name in input().split(", ")}

command = input()

while command != "End":
    hero, item, price = command.split("-")

    if item not in my_dict[hero][0]:
        my_dict[hero][0].append(item)
        my_dict[hero][1].append(int(price))
    command = input()

result = [print(f"{key} -> Items: {len(value[0])}, Cost: {sum(value[1])}") for key, value in my_dict.items()]