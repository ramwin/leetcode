#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
水域大小
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/pond-sizes-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import logging


LOGGER = logging.getLogger(__name__)


class Point:
    """坐标"""
    type = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WaterPoint(Point):
    """水域"""
    type = 0

    def __init__(self, x, y):
        super().__init__(x, y)
        self.pool = None  # 水域对应的池塘


class Pool():
    """池塘"""

    def __init__(self):
        # self.water_point_set = set()  # 池塘要记录有哪些水域
        # 第一次优化, 移除不需要的water_point_set, 1072ms => 932ms
        self.current_edges = set()  # BFS边缘
        self.size = 0

    def add_point(self, point: WaterPoint, init=False):
        """把某个水域添加到池塘"""
        point.pool = self
        # self.water_point_set.add(point)
        self.size += 1
        if init:
            self.current_edges = {point}

    # @property
    # def size(self):
    #     """返回池塘的大小"""
    #     return len(self.water_point_set)

    def add_all_points(self, matrix):
        """
        把池塘内所有的水域添加进来
        BFS 寻找边缘水域的相邻水域是否存在.
            如果存在, 当作新的边缘. 继续寻找
        """
        new_edges = set()
        for water_point in self.current_edges:
            # for neighbour in self.get_nearby_water_points(
            for neighbour in self.get_nearby_no_pool_water_points(
                    matrix, water_point.x, water_point.y):
                if neighbour.pool is not None:
                    LOGGER.info("这个水域已经属于当前池塘了,不用继续寻找")
                    continue
                self.add_point(neighbour)
                new_edges.add(neighbour)
        if new_edges:
            self.current_edges = new_edges
            self.add_all_points(matrix)

    @staticmethod
    def get_nearby_no_pool_water_points(matrix, x, y):
        """找到地图matrix坐标x,y附近的所有水域"""
        results = []
        max_x = len(matrix) - 1
        min_x = 0
        max_y = len(matrix[0]) - 1
        min_y = 0
        if x > min_x:
            point = matrix[x-1][y]
            if point.type == 0 and point.pool is None:
                results.append(point)
        if y > min_y:
            point = matrix[x][y-1]
            if point.type == 0 and point.pool is None:
                results.append(point)
        if x < max_x:
            point = matrix[x+1][y]
            if point.type == 0 and point.pool is None:
                results.append(point)
        if y < max_y:
            point = matrix[x][y+1]
            if point.type == 0 and point.pool is None:
                results.append(point)
        if (x < max_x) and (y < max_y):
            point = matrix[x+1][y+1]
            if point.type == 0 and point.pool is None:
                results.append(point)
        if (x > min_x) and (y > min_y):
            point = matrix[x-1][y-1]
            if point.type == 0 and point.pool is None:
                results.append(point)
        if (x < max_x) and (y > min_y):
            point = matrix[x+1][y-1]
            if point.type == 0 and point.pool is None:
                results.append(point)
        if (x > min_x) and (y < max_y):
            point = matrix[x-1][y+1]
            if point.type == 0 and point.pool is None:
                results.append(point)
        return results


class Solution1:
    """
    执行用时： 1072 ms , 在所有 Python3 提交中击败了 5.04% 的用户
    内存消耗： 76.8 MB , 在所有 Python3 提交中击败了 5.04% 的用户
    解法: 遍历所有的坐标.
    如果该坐标是水域(0), 就判断:
        1. 如果已经属于某个池塘了,就跳过
        2. 如果不属于池塘, 就创建一个新的池塘. 并且把
            池塘内所有的点设置为属于这个池塘
    """

    def __init__(self, maps):
        self.matrix = self.create_matrix_from_map(maps)
        self.pools = []  # 所有的池塘

    def create_matrix_from_map(self, maps):
        """把数字的二位数组, 变成Point的二位数组"""
        matrix = []
        for x, row in enumerate(maps):
            matrix_row = []
            for y, point_value in enumerate(row):
                point = self.create_point(
                    point_value,
                    x, y
                )
                matrix_row.append(point)
            matrix.append(matrix_row)
        return matrix

    @staticmethod
    def create_point(point_value, x, y):
        """根据数字和x,y创建点"""
        if point_value == 0:
            return WaterPoint(x, y)
        return Point(x, y)

    def get_pools_size(self):
        """返回所有池塘的列表"""
        for row in self.matrix:
            for point in row:
                if isinstance(point, WaterPoint):
                    if point.pool is not None:
                        continue
                    pool = Pool()
                    pool.add_point(point, init=True)
                    pool.add_all_points(self.matrix)
                    self.pools.append(pool)

        results = []
        for pool in self.pools:
            results.append(pool.size)
        results.sort()
        return results


class Solution:
    def pondSizes(self, land):
        return Solution1(land).get_pools_size()
