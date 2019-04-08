给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5

================================================================


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return  len(s.split( )[-1])  if(len(s.split( ))!=0) else 0
        

# 关键是 split（ ）和 split（‘ ’）的区别

>>> 'a '.split( )
['a']
>>>
>>> 'a '.split(" ")
['a', '']
>>>
===================================================================

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        words.reverse()
        init = 0
        for i in words:
            if i != '':
                init = len(i)
                break
        return init
        
