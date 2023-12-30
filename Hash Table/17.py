class Solution(object):
    def __init__(self) :
        self.ans = []
    def solve(self, digits, arr, i, com):
        if i == len(digits):
            return self.ans.append(com)
        c = digits[i]
        a = arr[int(c)]
        for x in a:
            self.solve(digits, arr, i+1, com + x)
    
    def letterCombinations(self, digits):
        a = []
        if not digits:
            return a
        arr = ["0", "0", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.solve(digits, arr, 0, "")
        return self.ans
        