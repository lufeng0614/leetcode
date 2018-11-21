#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@Author:     lufeng
@Contact:    lufeng0614@163.com
@Time:       2018/11/9  16:34
@note：      leetcode 892
"""
import numpy as np
import pandas as pd

from pandas import DataFrame
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid_array = np.array(grid)
        grid_df = pd.DataFrame(grid_array)

        print grid_df

        shape = grid_df.shape

        c = shape[0]
        w = shape[1]

        for i in range(0, shape[0]):
            for j in range(0, shape[1]):
                grid_df = grid_df[i][j]

        f_b = l_r = u_d = 0

        l_r = 2 * sum(grid_df.apply(np.max, axis=0))  # 左右
        f_b = 2 * sum(grid_df.apply(np.max, axis=1))  # 前后
        u_d = 2 * c * w  # 上下

        # 上下
        u_d = u_d - sum((grid_df == 0).astype(int).sum(axis=1)) * 2

        # 前后
        for i in range(1, shape[0]-1):
            for j in range(0, shape[1]):
                if grid_df[i-1][j] > grid_df[i][j] and  grid_df[i+1][j] > grid_df[i][j]:
                    qaz = abs(grid_df[i-1][j] - grid_df[i][j])
                    wsx = abs(grid_df[i+1][j] - grid_df[i][j])
                    f_b = f_b + min(qaz, wsx) * 2
        # 左右
        for i in range(0, shape[0]):
            for j in range(1, shape[1] - 1):
                if grid_df[i][j - 1] > grid_df[i][j] and grid_df[i][j + 1] > grid_df[i][j]:
                    qaz = abs(grid_df[i][j - 1] - grid_df[i][j])
                    wsx = abs(grid_df[i][j] - grid_df[i][j + 1])
                    l_r = l_r + min(qaz, wsx) * 2

        result = u_d + f_b + l_r
        return result




