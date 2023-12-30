class Solution(object):
    def closeStrings(self, word1, word2):
        charSet = set(word1)
        if len(word1) != len(word2) or charSet != set(word2):
            return False
        freq1 = []
        freq2 = []
        for c in charSet:
            freq1.append(word1.count(c))
            freq2.append(word2.count(c))
        freq1.sort()
        freq2.sort()
        return False if any(freq1[i] != freq2[i] for i in range(len(freq1))) else True


        # return sorted(Counter(word1).values()) == sorted(Counter(word2).values()) \
        # and set(word1) == set(word2)