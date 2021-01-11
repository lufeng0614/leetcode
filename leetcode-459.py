import re
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
         return True if re.fullmatch(r'([a-z]+)\1+',s) else False
         





import re
s1='abcabccba'
a=re.match(r'([a-z]+)\1+',s1)
print(a)
print(a.group())
print('\n')

s2='abcabcabc'
b=re.match(r'([a-z]+)\1+',s2)
print(b)
print(b.group())
print('\n')

c=re.fullmatch(r'([a-z]+)\1+',s1)
print(c)
print('\n')

d=re.fullmatch(r'([a-z]+)\1+',s2)
print(d)
print(d.group())


kmp解题思路
https://leetcode-cn.com/problems/repeated-substring-pattern/solution/kmp-python3jie-ti-si-lu-by-jackwener/
