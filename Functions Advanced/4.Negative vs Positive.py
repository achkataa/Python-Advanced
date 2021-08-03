def find_sum_of_lists(nums):

    positive = sum(filter(lambda x: x > 0, nums))
    negative = sum(filter(lambda x: x < 0, nums))

    print(negative)
    print(positive)


    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = list(map(int, input().split()))

find_sum_of_lists(numbers)





