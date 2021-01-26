class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        d = collections.defaultdict(int)   
        # step1     
        for i,j in dominoes:
            num = 10 * i + j if i < j else 10 * j+ i
            d[num] += 1
        # step2
        for k in d.values():
            ans += int(k*(k-1)/2)
        return ans

