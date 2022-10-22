#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
3 x 3 的幻方是一个填充有 从 1 到 9  的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。

给定一个由整数组成的row x col 的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/magic-squares-in-grid
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


NUMS = {1, 2, 3, 4, 5, 6, 7, 8, 9}


class Solution1:
    """
    执行用时： 48 ms , 在所有 Python3 提交中击败了 14.75% 的用户
    内存消耗： 15 MB , 在所有 Python3 提交中击败了 36.07% 的用户
    """

    def __init__(self, matrix):
        """
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        matrix左上角为(x=0, y=0)
        [
            [1, 2, 3]  y=0
            [4, 5, 6]  x= 1, 2, 3
        ]
        获取(x, y) 应该是 matrix[y][x]
        以3x3子矩阵的中心坐标, 作为子矩阵的坐标
        """
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)

    def get_result(self):
        result = 0
        for x in range(1, self.width-1):
            for y in range(1, self.height-1):
                if self.is_special(x, y):
                    result += 1
        return result

    def is_special(self, x, y):
        """
        判断中心坐标为(x,y)的矩阵, 是不是幻方矩阵
        """
        # 判断是不是1-9
        nums = set()
        for delta_y in range(-1, 2):
            for delta_x in range(-1, 2):
                nums.add(
                    self.matrix[y+delta_y][x+delta_x]
                )
        if nums != NUMS:
            return False

        # 第一列
        _sum0 = sum((
            self.matrix[y-1][x-1],
            self.matrix[y][x-1],
            self.matrix[y+1][x-1],
        ))
        # 第二列
        _sum1 = sum((
            self.matrix[y-1][x],
            self.matrix[y][x],
            self.matrix[y+1][x],
        ))
        if _sum0 != _sum1:
            return False
        # 第三列
        _sum2 = sum((
            self.matrix[y-1][x+1],
            self.matrix[y][x+1],
            self.matrix[y+1][x+1],
        ))
        if _sum2 != _sum0:
            return False
        # 第一行
        _sum3 = sum((
            self.matrix[y-1][x-1],
            self.matrix[y-1][x],
            self.matrix[y-1][x+1],
        ))
        if _sum3 != _sum0:
            return False
        # 第二行
        _sum4 = sum((
            self.matrix[y][x-1],
            self.matrix[y][x],
            self.matrix[y][x+1],
        ))
        if _sum4 != _sum0:
            return False
        # 第三行
        _sum5 = sum((
            self.matrix[y+1][x-1],
            self.matrix[y+1][x],
            self.matrix[y+1][x+1],
        ))
        if _sum5 != _sum0:
            return False
        # 反斜杠
        _sum6 = sum((
            self.matrix[y-1][x-1],
            self.matrix[y][x],
            self.matrix[y+1][x+1],
        ))
        if _sum6 != _sum0:
            return False
        # 正斜杠
        _sum7 = sum((
            self.matrix[y-1][x+1],
            self.matrix[y][x],
            self.matrix[y+1][x-1],
        ))
        if _sum7 != _sum0:
            return False
        return True


class Solution2:
    """
    优化: 中间的指必须是5
    执行用时： 40 ms , 在所有 Python3 提交中击败了 59.02% 的用户
    内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 6.56% 的用户
    """

    def __init__(self, matrix):
        """
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        matrix左上角为(x=0, y=0)
        [
            [1, 2, 3]  y=0
            [4, 5, 6]  x= 1, 2, 3
        ]
        获取(x, y) 应该是 matrix[y][x]
        以3x3子矩阵的中心坐标, 作为子矩阵的坐标
        """
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)

    def get_result(self):
        result = 0
        for x in range(1, self.width-1):
            for y in range(1, self.height-1):
                if self.is_special(x, y):
                    result += 1
        return result

    def is_special(self, x, y):
        """
        判断中心坐标为(x,y)的矩阵, 是不是幻方矩阵
        """
        if self.matrix[y][x] != 5:
            return False
        # 判断是不是1-9
        nums = set()
        for delta_y in range(-1, 2):
            for delta_x in range(-1, 2):
                nums.add(
                    self.matrix[y+delta_y][x+delta_x]
                )
        if nums != NUMS:
            return False

        # 第一列
        _sum0 = sum((
            self.matrix[y-1][x-1],
            self.matrix[y][x-1],
            self.matrix[y+1][x-1],
        ))
        # 第二列
        _sum1 = sum((
            self.matrix[y-1][x],
            self.matrix[y][x],
            self.matrix[y+1][x],
        ))
        if _sum0 != _sum1:
            return False
        # 第三列
        _sum2 = sum((
            self.matrix[y-1][x+1],
            self.matrix[y][x+1],
            self.matrix[y+1][x+1],
        ))
        if _sum2 != _sum0:
            return False
        # 第一行
        _sum3 = sum((
            self.matrix[y-1][x-1],
            self.matrix[y-1][x],
            self.matrix[y-1][x+1],
        ))
        if _sum3 != _sum0:
            return False
        # 第二行
        _sum4 = sum((
            self.matrix[y][x-1],
            self.matrix[y][x],
            self.matrix[y][x+1],
        ))
        if _sum4 != _sum0:
            return False
        # 第三行
        _sum5 = sum((
            self.matrix[y+1][x-1],
            self.matrix[y+1][x],
            self.matrix[y+1][x+1],
        ))
        if _sum5 != _sum0:
            return False
        # 反斜杠
        _sum6 = sum((
            self.matrix[y-1][x-1],
            self.matrix[y][x],
            self.matrix[y+1][x+1],
        ))
        if _sum6 != _sum0:
            return False
        # 正斜杠
        _sum7 = sum((
            self.matrix[y-1][x+1],
            self.matrix[y][x],
            self.matrix[y+1][x-1],
        ))
        if _sum7 != _sum0:
            return False
        return True


class Solution3:
    """
    优化: 避免计算中间的值
    执行用时： 28 ms , 在所有 Python3 提交中击败了 100.00% 的用户
    内存消耗： 15.4 MB , 在所有 Python3 提交中击败了 6.56% 的用户
    """

    def __init__(self, matrix):
        """
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        matrix左上角为(x=0, y=0)
        [
            [1, 2, 3]  y=0
            [4, 5, 6]  x= 1, 2, 3
        ]
        获取(x, y) 应该是 matrix[y][x]
        以3x3子矩阵的中心坐标, 作为子矩阵的坐标
        """
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)

    def get_result(self):
        result = 0
        for x in range(1, self.width-1):
            for y in range(1, self.height-1):
                if self.is_special(x, y):
                    result += 1
        return result

    def is_special(self, x, y):
        """
        判断中心坐标为(x,y)的矩阵, 是不是幻方矩阵
        """
        if self.matrix[y][x] != 5:
            return False
        # 判断是不是1-9
        nums = set()
        for delta_y in range(-1, 2):
            for delta_x in range(-1, 2):
                nums.add(
                    self.matrix[y+delta_y][x+delta_x]
                )
        if nums != NUMS:
            return False

        # 第一列
        _sum0 = sum((
            self.matrix[y-1][x-1],
            self.matrix[y][x-1],
            self.matrix[y+1][x-1],
            -5,
        ))
        # 第二列
        _sum1 = sum((
            self.matrix[y-1][x],
            self.matrix[y+1][x],
        ))
        if _sum0 != _sum1:
            return False
        # 第三列
        _sum2 = sum((
            self.matrix[y-1][x+1],
            self.matrix[y][x+1],
            self.matrix[y+1][x+1],
            -5,
        ))
        if _sum2 != _sum0:
            return False
        # 第一行
        _sum3 = sum((
            self.matrix[y-1][x-1],
            self.matrix[y-1][x],
            self.matrix[y-1][x+1],
            -5,
        ))
        if _sum3 != _sum0:
            return False
        # 第二行
        _sum4 = sum((
            self.matrix[y][x-1],
            self.matrix[y][x+1],
        ))
        if _sum4 != _sum0:
            return False
        # 第三行
        _sum5 = sum((
            self.matrix[y+1][x-1],
            self.matrix[y+1][x],
            self.matrix[y+1][x+1],
            -5,
        ))
        if _sum5 != _sum0:
            return False
        # 反斜杠
        _sum6 = sum((
            self.matrix[y-1][x-1],
            self.matrix[y+1][x+1],
        ))
        if _sum6 != _sum0:
            return False
        # 正斜杠
        _sum7 = sum((
            self.matrix[y-1][x+1],
            self.matrix[y+1][x-1],
        ))
        if _sum7 != _sum0:
            return False
        return True


class Solution:
    """题目给的框架"""
    def numMagicSquaresInside(self, grid) -> int:
        return Solution2(grid).get_result()
