#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@Author:     lufeng
@Contact:    lufeng0614@163.com
@Time:       2018/11/8  15:46
@note：      leetcode 7
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        def revs(x):
            last = rev = 0
            while (x != 0):
                last = x % 10
                x = x / 10
                if x != 0:
                    if x < 10:
                        rev = rev + last
                    else:
                        rev = (rev + last) * 10
                else:
                    rev = rev * 10 + last
            return rev

        if x >= 0:
            rev = revs(x)
        else:
            rev = revs(abs(x)) * -1

        if abs(rev) > (2**31 - 1):
            return 0
        else:
            return rev

