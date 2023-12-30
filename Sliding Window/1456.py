class Solution(object):
    def maxVowels(self, s, k):
        vowels = 'aeiou'
        currCount, ans = 0, 0
        for i in range(len(s)):
            currCount += s[i] in vowels
            if i >= k and s[i-k] in vowels:
                currCount -= 1
            ans = max(ans, currCount)
        return ans

