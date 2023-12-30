class Solution(object):
    def trap(self, height):
        left, right = 0, len(height)-1
        lmax, rmax, water = height[left], height[right], 0
        while left <= right:
            if height[left] < height[right]:
                if height[left] < lmax:
                    water += lmax - height[left]
                else:
                    lmax = height[left]
                left += 1
            else:
                if height[right] < rmax:
                    water += rmax - height[right]
                else:
                    rmax = height[right]
                right -= 1

        return water

