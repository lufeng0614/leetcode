class Solution(object):
    def tohex(self, num: int) -> str:
        """
        :param num:
        :return:
        """
        # return str('{:x}'.format(num))
        return hex(num & 0xFFFFFFFF)[2:]

    """
    def toHex(self, num: int) -> str:
        num &= 0xFFFFFFFF    python求补码
        s = "0123456789abcdef"
        res = ""
        mask = 0b1111
        while num > 0:
            res += s[num & mask]
            num >>= 4
        return res[::-1] if res else "0"
    
    链接：https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/solution/pythonqiu-jie-by-powcai/

    """


if __name__ == '__main__':
    num = -1
    print(Solution().tohex(num))
