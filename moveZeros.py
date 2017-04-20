class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)


numsList = Solution()
numsList.moveZeroes([1, 3, 4, 5, 31, 0, 13, 0, 3])
print(numsList.nums)
