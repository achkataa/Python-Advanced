n_queries = int(input())

stack = []
result = []

for query in range(n_queries):
    new_query = input().split()
    command = int(new_query[0])

    if command == 1:
        number = int(new_query[1])
        stack.append(number)

    elif command == 2:
        if stack:
            stack.pop()

    elif command == 3:
        if stack:
            print(max(stack))

    elif command == 4:
        if stack:
            print(min(stack))

while stack:
    result.append(stack.pop())

result = [str(res) for res in result]
print(", ".join(result))