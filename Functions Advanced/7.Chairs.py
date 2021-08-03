# def calc_combinations(names, n, combs = []):
#     if len(combs) == n:
#         print(', '.join(combs))
#         return
#
#     for i in range(len(names)):
#         name = names[i]
#         combs.append(name)
#         calc_combinations(names[i+1:], n, combs)
#         combs.pop()
#
#
#
# names = input().split(", ")
# n = int(input())
#
# calc_combinations(names, n)

# from itertools import combinations
#
#
#
# names = input().split(", ")
# n = int(input())
#
# print(*[', '.join(el) for el in combinations(names, n)], sep="\n")


def calc_combinations(names, n, combs = []):
    if len(combs) == n:
        print(', '.join(combs))
        return

    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        calc_combinations(names[i+1:], n, combs)
        combs.pop()



names = input().split(", ")
n = int(input())

calc_combinations(names, n)