给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false



==============================================================


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return False
        elif num==1:
            return True
        else:
            a=1
            while True:
                if a<num:
                    a=a*4
                if a==num:
                    return True
                if a>num:
                    return False
