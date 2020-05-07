class Solution(object):
    def addbinary(self, a: str, b: str) -> str:
        """
        :param a: 二进制字符串a
        :param b: 二进制字符串b
        :return: a+b 二进制表示
        """
        print("十进制a:", int(a, 2))
        print("十进制b:", int(b, 2))
        print("二进制a:", bin(int(a, 2)))  # 转二进制
        print("二进制b:", '{:b}'.format(3))  # 转二进制 link：https://www.cnblogs.com/xyou/p/10966460.html

        #
        int10_a = int(a, 2)
        int10_b = int(b, 2)

        int10_ab = int(a, 2) + int(b, 2)
        return str('{:b}'.format(int10_ab))


if __name__ == '__main__':
    a = '11'
    b = '1'
    print(Solution().addbinary(a, b))

