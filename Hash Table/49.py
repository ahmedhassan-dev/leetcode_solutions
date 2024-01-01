class Solution(object):
    def groupAnagrams(self, strs):
        anagram_dic = {}
        for word in strs:
            k = "".join(sorted(word))
            if k not in anagram_dic:
                anagram_dic[k] = [word]
            else:
                anagram_dic[k].append(word)

        return list(anagram_dic.values())