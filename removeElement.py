'''Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        self.nums = nums
        self.val = val

        for num in self.nums:
            if num == val:
                self.nums.remove(num)

        return len(self.nums)

element_list = Solution()

list1 = [1, 3, 4, 2, 3, 4]
list2 = [3, 3]
list3 = [3, 3, 3]
list4 = [3, 1, 2, 3]

element_list.removeElement(list1, 3)
element_list.removeElement(list2, 3)
element_list.removeElement(list3, 3)
element_list.removeElement(list4, 3)

print("Test 1", len(list1))
print("Test 2", len(list2))
print("Test 3", len(list3))
print("Test 4", len(list4))
