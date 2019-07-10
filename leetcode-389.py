给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。



class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #方法一：异或
        result = 0
        for i in s + t:
           result = result ^ ord(i)
        return chr(result)
        
        #方法二：减法
        # return chr(sum([ord(i) for i in t]) - sum([ord(j) for j in s]))
