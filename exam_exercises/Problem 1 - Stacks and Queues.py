from collections import deque

firework_effects = deque([int(num) for num in input().split(", ")])
explosive_power = [int(num) for num in input().split(", ")]

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while firework_effects and explosive_power:
    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    mix = firework_effects[0] + explosive_power[-1]

    if mix % 3 == 0 and mix % 5 != 0:
        palm_firework += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif mix % 5 == 0 and mix % 3 != 0:
        willow_firework += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif mix % 3 == 0 and mix % 5 == 0:
        crossette_firework += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        current_effect = firework_effects.popleft()
        firework_effects.append(current_effect - 1)



if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(num) for num in firework_effects)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(num) for num in explosive_power)}")


print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")












