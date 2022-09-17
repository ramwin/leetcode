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


class Point:
    """坐标"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WaterPoint(Point):
    """水域"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.pool = None  # 水域对应的池塘


class Pool():
    """池塘"""

    def __init__(self):
        self.water_point_set = set()  # 池塘要记录有哪些水域

    def add_point(self, point: WaterPoint):
        """把某个水域添加到池塘"""
        point.pool = self
        self.water_point_set.add(point)

    @property
    def size(self):
        """返回池塘的大小"""
        return len(self.water_point_set)

    def add_all_points(self):
        """把池塘内所有的水域添加进来"""
        raise NotImplementedError


class Solution1:
    """
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
        raise NotImplementedError

    def get_pools_size(self):
        """返回所有池塘的列表"""
        for row in self.matrix:
            for point in row:
                if isinstance(point, WaterPoint):
                    if point.pool is not None:
                        continue
                    pool = Pool()
                    pool.add_point(point)
                    pool.add_all_points()
                    self.pools.append(pool)

        results = []
        for pool in self.pools:
            results.append(pool.size)
        results.sort()
        return results
