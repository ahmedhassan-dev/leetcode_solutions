class Solution(object):
    def reverseOnlyLetters(self, s):
        left, right = 0, len(s) - 1
        l = list(s)
        while left < right:
            if l[left].isalpha():
                if l[right].isalpha():
                    l[left], l[right] = l[right], l[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
       
        return "".join(l)

        