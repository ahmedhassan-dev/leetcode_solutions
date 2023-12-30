class Solution(object):
    def isSubsequence(self, s, t):
        sn, tn = len(s), len(t)
        si = 0
        for ti in xrange(tn):
            if sn == si: return True
            if s[si] == t[ti]:
                si += 1
        return si == sn
