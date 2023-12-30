class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        ans, prev = 0, float("-inf")
        intervals = sorted(intervals, key=lambda a : a[1])
        for i in intervals:
            if prev <= i[0]:
                prev = i[1] 
            else:
                ans += 1
        return ans
