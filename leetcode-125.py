给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

========================================================================

class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ''.join(filter(str.isalnum, s.lower()))  == 关键是join的应用
        return reverse == reverse[::-1]
       
  
  
  class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = list(filter(str.isalnum, s.lower()))  == 关键是join的应用
        return reverse == reverse.reverse()
        我的方法会报错
