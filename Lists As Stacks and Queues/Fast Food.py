from collections import deque
food = int(input())

orders = [int(order) for order in input().split()]

queue = deque(orders)

print(max(queue))




