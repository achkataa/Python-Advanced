from collections import deque

cups = [int(cup) for cup in input().split()]

cups = deque(cups)

bottles = [int(bottle) for bottle in input().split()]

wasted_water = 0

cups_left = []
bottles_left = []

while cups:
    cup = cups[0]

    if bottles:
        bottle = bottles.pop()
        if bottle < cup:
            cup -= bottle
            while cup > 0:
                bottle = bottles.pop()
                cup -= bottle
            if cup < 0:
                wasted_water += abs(cup)
            cups.popleft()
        else:
            current_wasted_water = bottle - cup
            wasted_water += current_wasted_water
            cups.popleft()
    else:
        for cup in cups:
            cups_left.append(str(cup))
        print(f"Cups: {' '.join(cups_left)}")
        print(f"Wasted litters of water: {wasted_water}")
        exit(0)

for bottle in reversed(bottles):
    bottles_left.append(str(bottle))
print(f"Bottles: {' '.join(bottles_left)}")
print(f"Wasted litters of water: {wasted_water}")



