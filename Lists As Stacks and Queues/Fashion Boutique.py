box = [int(clothes) for clothes in input().split()]

rack_capacity = int(input())

current_capacity = rack_capacity
counter = 1


while box:
    current_clothes = box.pop()
    if current_clothes <= current_capacity:
        current_capacity -= current_clothes

    else:
        counter += 1
        current_capacity = rack_capacity
        current_capacity -= current_clothes

print(counter)








