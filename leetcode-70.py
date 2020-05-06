def factorial(x):
    """
    :param x: 阶乘
    :return: x的阶乘
    """
    k = 1
    for i in range(1, x+1):
        k = k * i
    return k


def combination(n, b):
    """
    :param n: n阶楼梯
    :param b: b个2步
    :return: 组合数
    """
    comb = factorial(n-b) / (factorial(b) * factorial(n-2*b))
    return comb


class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        for i in range(0, n//2+1):
            ans = ans + combination(n, i)
        return int(ans)
