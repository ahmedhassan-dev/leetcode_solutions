from collections import deque


class Solution(object):
    def dailyTemperatures(self, T):
        # Time Complexity : O(N)
        # Space Complexity : O(N)
        ans, s = [0] * len(T), deque()
        for cur, cur_temp in enumerate(T):
            while s and T[s[-1]] < cur_temp:
                ans[s[-1]] = cur - s[-1]
                s.pop()
            s.append(cur)
        return ans