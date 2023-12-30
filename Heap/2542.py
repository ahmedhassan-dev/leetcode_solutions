class Solution(object):
    def maxScore(self, nums1, nums2, k):
        h, score, curr_sum = [], 0, 0
        A = sorted(zip(nums1, nums2), key = lambda x: -x[1])
        for num1, num2 in A:
            heapq.heappush(h, num1)
            curr_sum += num1
            if len(h) == k:
                score = max(score, num2 * curr_sum)
                curr_sum -= heapq.heappop(h)
        return score
