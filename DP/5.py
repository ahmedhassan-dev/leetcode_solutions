class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1 or s == s[::-1]:
            return s
        start, len_of_temp = 0, 1
        for i in range(1, len(s)):
            odd = s[i-len_of_temp-1: i+1]
            even = s[i-len_of_temp: i+1]
            if i-len_of_temp-1 >= 0 and odd == odd[::-1]:
                start = i-len_of_temp-1
                len_of_temp += 2
                continue
            if even == even[::-1]:
                start = i-len_of_temp
                len_of_temp += 1
        return s[start: start+len_of_temp]