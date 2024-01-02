class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums: #Looking for the smallest num
                y = x + 1         #Getting the sec smallest num
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

        