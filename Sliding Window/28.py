class Solution(object):
    def strStr(self, haystack, needle):
        i, d, ans = 0, len(needle), -1
        while i+d <= len(haystack):
            wdw = haystack[i:i+d]
            if wdw == needle:
                return i
            else:
                i += 1
        return -1
