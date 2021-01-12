import re
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c_sum = int(bin(x)[2:]) + int(bin(y)[2:])
        return len(re.findall(r'1', str(c_sum)))
