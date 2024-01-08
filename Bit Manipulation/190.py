class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        out = 0
        for _ in range(31):
            bit = n & 1
            out |= bit
            out <<= 1
            n >>= 1
        out |= n
        return out