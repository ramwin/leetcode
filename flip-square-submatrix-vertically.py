#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
https://leetcode.cn/problems/flip-square-submatrix-vertically/description/?envType=daily-question&envId=2026-03-21

给你一个 m x n 的整数矩阵 grid，以及三个整数 x、y 和 k。

整数 x 和 y 表示一个 正方形子矩阵 的左上角下标，整数 k 表示该正方形子矩阵的边长。

你的任务是垂直翻转子矩阵的行顺序。

返回更新后的矩阵。


输入： grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3

输出： [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]


输入： grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2

输出： [[3,4,4,2],[2,3,2,3]]
"""

from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        """
        垂直翻转子矩阵的行顺序（原地修改，O(1) 额外空间）
        """
        n_cols = len(grid[0]) if grid else 0
        
        # 子矩阵的列范围
        left_col, right_col = y, y + k
        
        # 策略选择：k 较大时先交换整行再修复，k 较小时直接逐元素交换
        if k > n_cols // 2:
            # 策略1：先交换整行，再修复不在子矩阵内的列
            for offset in range(k // 2):
                top_row = x + offset
                bottom_row = x + k - 1 - offset
                # 先交换整行（Python 层面的高效操作）
                grid[top_row], grid[bottom_row] = grid[bottom_row], grid[top_row]
                # 修复左侧不在子矩阵内的列
                for col in range(left_col):
                    grid[top_row][col], grid[bottom_row][col] = \
                        grid[bottom_row][col], grid[top_row][col]
                # 修复右侧不在子矩阵内的列
                for col in range(right_col, n_cols):
                    grid[top_row][col], grid[bottom_row][col] = \
                        grid[bottom_row][col], grid[top_row][col]
        else:
            # 策略2：k 较小，直接逐元素交换子矩阵内的元素
            for offset in range(k // 2):
                top_row = x + offset
                bottom_row = x + k - 1 - offset
                for col in range(left_col, right_col):
                    grid[top_row][col], grid[bottom_row][col] = \
                        grid[bottom_row][col], grid[top_row][col]
        
        return grid


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例 1
    grid1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    x1, y1, k1 = 1, 0, 3
    print(f"输入: grid = {grid1}, x = {x1}, y = {y1}, k = {k1}")
    result1 = solution.reverseSubmatrix(grid1, x1, y1, k1)
    print(f"输出: {result1}")
    print(f"预期: [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]")
    print()
    
    # 测试用例 2
    grid2 = [[3,4,2,3],[2,3,4,2]]
    x2, y2, k2 = 0, 2, 2
    print(f"输入: grid = {grid2}, x = {x2}, y = {y2}, k = {k2}")
    result2 = solution.reverseSubmatrix(grid2, x2, y2, k2)
    print(f"输出: {result2}")
    print(f"预期: [[3,4,4,2],[2,3,2,3]]")

