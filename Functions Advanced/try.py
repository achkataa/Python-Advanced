# def a(n):
#     if n >= 1:
#         a(n-1)
#         print(n)
#
# a(3)


# def factorial(x):
#
#     if x == 1:
#         return 1
#     else:
# #         return (x * factorial(x-1))
# #
# #
# # num = 4
# # print(factorial(num))
#
#
#
# def factorial(x):
#
#     if x == 1:
#         return 1
#     return (x * factorial(x - 1))
#
#
# num = 3
# print(factorial(num))

def say_hello(times):

    if times == 0:
        return
    print("Hello")
    return say_hello(times-1)

say_hello(5)



