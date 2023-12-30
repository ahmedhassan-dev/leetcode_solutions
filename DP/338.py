class Solution(object):
    def countBits(self, n):
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            if i % 2 == 0:
                res[i] = res[i // 2]
            else:
                res[i] = 1 + res[i // 2]
            print(res[4])
        return res
        # counter = [0]
        # for i in range(1, n+1):
        #     counter.append(counter[i >> 1] + i % 2)
        # return counter

        