from collections import deque

people = input().split()

step = int(input())

queue = deque(people)

while len(queue) > 1:
    for i in range(step - 1):
        queue.append(queue.popleft())
    print(f"Removed {queue.popleft()}")

print(f"Last is {queue.popleft()}")





