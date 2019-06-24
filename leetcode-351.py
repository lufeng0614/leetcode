编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。


==========================================================================================
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = ['a','e','i','o','u','A','E','I',"O","U"]
        vowel_local = []
        s = list(s)
        for i in range(len(s)):

            if s[i] in vowel:

                vowel_local.append(i)

        for i in range(len(vowel_local)//2):

            s[vowel_local[i]], s[vowel_local[-i-1]] = s[vowel_local[-i-1]],s[vowel_local[i]]

        return "".join(s)
