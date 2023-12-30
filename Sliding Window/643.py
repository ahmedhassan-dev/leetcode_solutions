class Solution(object):
    def findMaxAverage(self, nums, k):
        max_sum = sum(nums[:k])
        new_sum = max_sum
        for i in range(k, len(nums)):
            new_sum = new_sum - nums[i-k] + nums[i]
            if new_sum > max_sum:
                max_sum = new_sum
        return (max_sum + .0) / k