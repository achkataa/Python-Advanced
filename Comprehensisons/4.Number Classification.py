numbers = [int(i) for i in input().split(", ")]

my_dict = {"Positive": [], "Negative": [], "Even": [], "Odd": []}

for num in numbers:
    if num > -1:
        my_dict["Positive"].append(num)
    if num <= -1:
        my_dict["Negative"].append(num)
    if num % 2 == 0:
        my_dict["Even"].append(num)
    if num % 2 != 0:
        my_dict["Odd"].append(num)


for key, value in my_dict.items():
    nums = ", ".join(str(v) for v in value)
    print(f"{key}: {nums}")
