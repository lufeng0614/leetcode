需要二刷

================================================================================
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"

=========================================================================================

class Solution:
    def countAndSay(self, n: int) -> str:
        dic = {
            1:"1",
            2:"11",
            3:"21",
            4:"1211",
            5:"111221"
        }
        if n <=5:
            return dic.get(n)
        for i in range(6,n+1):
            s = dic.get(i-1)
            res = ""
            c = 0
            pre = s[0]
            for j in range(len(s)):
                if s[j] == pre:
                    c += 1 
                else:
                    res += str(c)+pre                                        
                    pre = s[j]
                    c = 1
            res += str(c)+pre       
            dic[i] = res
            res = ""
        return dic.get(n)       
                        
                
            