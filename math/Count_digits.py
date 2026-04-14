import math
class Solution:
    def countDigit(self, n):
        n = int(math.log10(n)+1)
        return n