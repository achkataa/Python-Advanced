

from collections import deque


food_quantity = int(input())


quantity_of_orders = deque(int(i) for i in input().split(" "))

incomplete_orders = []

print(max(quantity_of_orders))

while quantity_of_orders:

    next_order = quantity_of_orders.popleft()


    if next_order <= food_quantity:

        food_quantity -= next_order
    else:

        incomplete_orders.append(next_order)
        break

if incomplete_orders:
    while quantity_of_orders:
        incomplete_orders.append(quantity_of_orders.popleft())
    print(f"Orders left: {' '.join([str(i) for i in incomplete_orders])}")
else:
    print(f"Orders complete")


