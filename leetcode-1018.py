class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        tmp = ''
        res = []
        for i in A:
            tmp = tmp+str(i)
            if int(tmp,2)%5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
