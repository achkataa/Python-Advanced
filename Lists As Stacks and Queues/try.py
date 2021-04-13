from collections import deque

people = input().split()

step = int(input())

queue = deque(people)
counter = 0
while len(queue) > 1:
    counter += 1

    if counter == step:
        print(f"Removed {queue.popleft()}")
        counter = 0
    else:
        queue.append(queue.popleft())

print(f"Last is {queue.popleft()}")






