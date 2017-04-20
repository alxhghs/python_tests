'''
Given five positive integers, find the minimum and maximum values that can be
calculated by summing exactly four of the five integers. Then print the
respective minimum and maximum values as a single line of two space-separated
long integers.
'''


def mini_max(*nums):
    num_list = []
    for num in nums:
        num_list.append(num)  # get the nums into a list
    num_list.sort()           # sort the nums
    max_sum = sum(num_list[1:])
    min_sum = sum(num_list[0:-1])
    print(max_sum, min_sum)


mini_max(1, 2, 5, 6, 4)

print("the answer should be: {}".format(2 + 5 + 6 + 4))
print("followed by: {}".format(1 + 2 + 4 + 5))
