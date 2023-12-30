class Solution(object):
    def uniqueOccurrences(self, arr):
        # c = Counter(arr)
        # cKeys = Counter(arr).keys()
        # cValues = Counter(arr).values()
        # cSet  = set(cValues)
        return len(Counter(arr).keys()) == len(set(Counter(arr).values()))
        