class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height)-1
        maxArea = 0
        while left < right:
            curArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, curArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea

        