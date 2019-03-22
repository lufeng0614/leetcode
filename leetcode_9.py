判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

=========================================================================

# 题解里的 除10 取余的 算法思路没太懂
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            list_x = list(str(x))
            list_x.reverse() # 关于reverse() 的理解也出错了
            for i in range(len(list_x)):
                if list(str(x))[i] != list_x[i]:
                    return False
                else:
                    if i != (len(list_x)-1): # 这里出错了
                        continue
                    else:
                        return True
            
