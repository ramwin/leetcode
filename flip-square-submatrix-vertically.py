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
        # 垂直翻转子矩阵：交换第 i 行和第 k-1-i 行
        for i in range(k // 2):
            for j in range(k):
                # 交换位置 (x + i, y + j) 和 (x + k - 1 - i, y + j) 的元素
                grid[x + i][y + j], grid[x + k - 1 - i][y + j] = \
                    grid[x + k - 1 - i][y + j], grid[x + i][y + j]
        
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

