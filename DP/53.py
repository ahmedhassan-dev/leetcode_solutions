class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]
        currentSum = nums[0]
        for num in nums[1:]:
            currentSum = max(num,num+currentSum)
            maxSum = max(currentSum,maxSum)
        return maxSum
        