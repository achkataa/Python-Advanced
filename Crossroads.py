from collections import deque
green_light_time = int(input())
free_window = int(input())
current_window = free_window
current_green_light = green_light_time
hit_char = ""

cars_passed = 0

queue = deque()

command = input()

while command != "END":
    if command == "green":
        current_green_light = green_light_time
        car = queue.popleft()
        car2 = car
        for char in car2:
            if current_green_light > 0:
                car2 = car2.replace(char, "", 1)
                current_green_light -= 1
            else:
                break
        if car2 == "":
            command = input()
            cars_passed += 1
            continue
        else:
            for char in car2:
                if current_window > 0:
                    car2 = car2.replace(char, "", 1)
                    current_window -= 1
                else:
                    hit_char = char
                    break
            if car2 == "":
                command = input()
                cars_passed += 1
                continue
            else:
                print("A crash happened!")
                print(f"{car2} was hit at {hit_char}.")
                exit(0)

    else:
        queue.append(command)



    command = input()

print("Everyone is safe.")
print(f"{cars_passed} total cars passed the crossroads.")