
# EX-1

# string = input()
#
# stack = []
#
# for char in string:
#     stack.append(char)
#
# while stack:
#     print(stack.pop(), end="")

# EX-2

# expression = input()
#
# stack = []
#
# for index in range(len(expression)):
#     if expression[index] == "(":
#         stack.append(index)
#     elif expression[index] == ")":
#         print(expression[stack.pop():index+1])

# EX-3

# from collections import deque
#
# command = input()
#
# queue = deque()
#
# while command != "End":
#     if command == "Paid":
#         while queue:
#             print(queue.popleft())
#     else:
#         queue.append(command)
#
#     command = input()
#
# print(f"{len(queue)} people remaining.")


# EX-4

# from collections import deque
# quantity_of_water = int(input())
#
# name = input()
#
# queue = deque()
#
# while name != "Start":
#     queue.append(name)
#
#     name = input()
#
# command = input()
#
#
# while command != "End":
#     data = command.split()
#     action = data[0]
#
#     if action.isdigit():
#         if quantity_of_water >= int(action):
#             print(f"{queue.popleft()} got water")
#             quantity_of_water -= int(action)
#         else:
#             print(f"{queue.popleft()} must wait")
#     else:
#         liters = int(data[1])
#         quantity_of_water += liters
#
#     command = input()
#
# print(f"{quantity_of_water} liters left")


# EX-5

# from collections import deque
# people = deque(input().split())
# toss = int(input())
#
# counter = 0
#
# while len(people) != 1:
#     counter += 1
#     if counter % toss == 0:
#         print(f"Removed {people.popleft()}")
#         continue
#     people.append(people.popleft())
#
# print(f"Last is {people.popleft()}")










