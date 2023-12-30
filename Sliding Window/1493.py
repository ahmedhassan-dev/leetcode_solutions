class Solution(object):
    def longestSubarray(self, nums):
        left, lastZero, maxWindow = 0, -1, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                left = lastZero + 1
                lastZero = right
            maxWindow = max(maxWindow, right-left)
        return maxWindow
            
        