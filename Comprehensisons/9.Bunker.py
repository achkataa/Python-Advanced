# food_categories = {category: ([], [], []) for category in input().split(", ")}
#
# n = int(input())
#
# for i in range(n):
#     category_and_product = input().split(" - ")
#     current_category = category_and_product[0]
#     product = category_and_product[1]
#     quantity_and_quality = category_and_product[2].split(";")
#     quantity_string = quantity_and_quality[0].split(":")
#     quantity = int(quantity_string[1])
#     quality_string = quantity_and_quality[1].split(":")
#     quality = int(quality_string[1])
#
#     if not product in food_categories[current_category][0]:
#         food_categories[current_category][0].append(product)
#         food_categories[current_category][1].append(quantity)
#         food_categories[current_category][2].append(quality)
#
# count_of_items = 0
# for key, value in food_categories.items():
#     count_of_items += sum(value[1])
#
# print(f"Count of items: {count_of_items}")
# total_quality = 0
# for key, value in food_categories.items():
#     total_quality += sum(value[2])
#
# print(f"Average quality: {total_quality / len(food_categories):.2f}")
#
# for key, value in food_categories.items():
#     print(f"{key} -> {', '.join(value[0])}")
#
#


food_categories = {category: ([], [], []) for category in input().split(", ")}

n = int(input())

for i in range(n):
    category_and_product = input().split(" - ")
    current_category = category_and_product[0]
    product = category_and_product[1]
    quantity_and_quality = category_and_product[2].split(";")
    quantity_string = quantity_and_quality[0].split(":")
    quantity = int(quantity_string[1])
    quality_string = quantity_and_quality[1].split(":")
    quality = int(quality_string[1])

    if not product in food_categories[current_category][0]:
        food_categories[current_category][0].append(product)
        food_categories[current_category][1].append(quantity)
        food_categories[current_category][2].append(quality)

count_of_items = 0
for key, value in food_categories.items():
    count_of_items += sum(value[1])

print(f"Count of items: {count_of_items}")
total_quality = 0
for key, value in food_categories.items():
    total_quality += sum(value[2])

print(f"Average quality: {total_quality / len(food_categories):.2f}")

for key, value in food_categories.items():
    print(f"{key} -> {', '.join(value[0])}")



