from collections import deque

queue = deque()
water_quantity = int(input())

names = input()

while names != "Start":
    queue.append(names)

    names = input()

command = input()

while command != "End":
    data = command.split()
    action = data[0]

    if action == "refill":
        water = int(data[1])
        water_quantity += water

    else:
        action = int(data[0])
        if water_quantity >= action:
            print(f"{queue.popleft()} got water" )
            water_quantity -= action
        else:
            print(f"{queue.popleft()} must wait")

    command = input()

print(f"{water_quantity} liters left")



