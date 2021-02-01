class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]: 
        diff = sum(B) - sum(A)
        dic = collections.Counter(A)
        for b in B:
            if b - diff // 2 in dic:
               return [b - diff // 2, b]

