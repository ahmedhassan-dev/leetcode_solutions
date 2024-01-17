class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
        res = []
        cnt = Counter(nums1)
        for x in nums2:
            if cnt[x] > 0:
                res.append(x)
                cnt[x] -= 1
        return res