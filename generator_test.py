numbers = [1, 2, 3, 4, 5]

# def num_list(numbers):
#     results = []
#     for i in num:
#         results.append(i*i)
#     return results


def num_generator(numbers):
    for i in numbers:
        yield (i*i)


my_nums = num_generator(numbers)

# print num_generator(numbers)

for num in my_nums:
    print num

# print num_list(numbers)
#
# print num_generator(numbers)
#
# print next(my_nums)
# print next(my_nums)

# print next(numbers)
