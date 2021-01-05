class Solution:
    def arrangeCoins(self, n: int) -> int:
        tmp = int((2*n) ** 0.5)
        while tmp*(tmp+1)> 2*n:
            tmp = tmp -1
        return tmp
        
        
========================================
class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = ((1+8*n)**0.5-1)/2
        return int(res)
数学。。。
