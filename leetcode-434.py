class Solution:
    def countSegments(self, s: str) -> int:
        aa = s.split(' ')
        while '' in aa:
            aa.remove('')
        return len(aa)
