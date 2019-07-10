给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.

======================================================================================

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
#         方法一
        d={}
        for i in s:
            if i not in d:
                d[i]=True
            else:
                d[i]=False
        for i in s:
            if d[i]==True:
                return s.index(i)
        return -1
    
#     方法二
        d = {c: s.count(c) for c in set(s)}
        return ([i for i, c in enumerate(s) if d[c] == 1] + [-1])[0]
