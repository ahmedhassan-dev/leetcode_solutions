class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        for i in range(1,n):
            result[i] = result[i-1] * nums[i-1]
        
        right_prod = 1
        for i in range(n-1,-1,-1):
            result[i] *=  right_prod
            right_prod *= nums[i]
        return result
