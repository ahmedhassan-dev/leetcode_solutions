class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums)-1
        while left < right-1:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] < nums[mid+1]:
                left +=1
            else:
                right-=1
        return left if nums[left] >= nums[right] else right

