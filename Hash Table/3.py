class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxl, left = 0, 0
        charMap = {}
        for right in range(len(s)):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxl = max(maxl, right - left +1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        return maxl