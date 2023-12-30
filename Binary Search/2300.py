class Solution(object):
    def successfulPairs(self, spells, potions, success):
        n, m = len(spells), len(potions)
        # Sort potions O(n*log(n))
        potions.sort()
        results = []
        for s in spells:
            minPotion = (success + s - 1) // s
            indx = bisect.bisect_left(potions,minPotion)
            results.append(m - indx)
        return results