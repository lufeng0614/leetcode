#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@Author:     lufeng
@Contact:    lufeng0614@163.com
@Time:       2018/11/9  16:16
@note：      leetcode 704
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        for i, num in enumerate(nums):
            if num != target:
                i += 1
                if num == nums[-1]:
                    return -1
            if num == target:
                return i
