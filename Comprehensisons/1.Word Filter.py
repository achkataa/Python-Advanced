words = input().split()

result = [w for w in words if len(w) % 2 == 0]

for res in result:
    print(res)