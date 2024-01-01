class Solution(object):
    def moveZeroes(self, nums):
       anchor = 0
       for ex in range(len(nums)):
           if nums[ex] != 0:
                nums[anchor], nums[ex] = nums[ex], nums[anchor]
                anchor += 1