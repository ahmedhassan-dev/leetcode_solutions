class Solution(object):
    def decodeString(self, s):
        stack, currentChar, k = [], [], 0
        for char in s:
            if char == "[":
                stack.append((currentChar, k))
                currentChar = []
                k = 0
            elif char == "]":
                lastChar, lastKey = stack.pop()
                currentChar = lastChar + lastKey * currentChar
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                currentChar += char
        return ''.join(currentChar)


            