#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@Author:     lufeng
@Contact:    lufeng0614@163.com
@Time:       2018/11/5  21:18
@note：      leetcode 848
"""

import sys


class Solution(object):
    def shiftingLetters(self, S, shifts):
        """

        :param S: letters string
        :param shifts: shifting list[int]
        :return: shifted S
        """

        """
        @ 以下代码在leetcode 测试执行，一直超出时间限制，查找原因是可能存在死循环
        @ 但是如何判断是死循环，还是代码有问题
        @
        
        s_len = len(S)
        # s_sum 总移动次数，即第一个字母移动次数，其他字母依次递减 sum(shifts[::j])

        new_S = ''
        for j in range(s_len):
            loc_s = ord(S[j]) + sum(shifts[j::]) % 26
            if loc_s > 122:
                loc_s = 96 + loc_s % 122
            new_S = new_S + chr(loc_s)
        """

        sum_loc = sum(shifts)
        loc_s = []
        for i in shifts:
            loc_s.append(sum_loc)
            sum_loc = sum_loc - i

        new = ''
        for i, s in enumerate(S):
            new_S = ord(s) + loc_s[i] % 26
            if new_S > 122:
                new_S = 96 + new_S % 122
            new = new + chr(new_S)

        return new_S





