class Solution(object):
    def searchInsert(self, nums, target):
        start , end = 0 , len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return end + 1
        