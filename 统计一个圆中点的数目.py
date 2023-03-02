#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
特意用最差的算法
一看, 才500个点, 直接遍历喽
再一看, 都是整数, 可以考虑遍历圆里面的点或者遍历圆的边

"""


from dataclasses import dataclass
import math

from typing import List


@dataclass
class Point:
    """点"""
    x: int
    y: int

    def get_distance(self, target: "Point"):
        # XXX 可以返回平方数, 用整数比较
        return math.sqrt(
            math.pow(self.x - target.x, 2)
            + math.pow(self.y - target.y, 2)
        )


@dataclass
class Cycle(Point):
    """圆"""
    r: int

    def contain(self, point: Point):
        return self.r >= self.get_distance(point)


@dataclass
class Map:
    """地图"""

    points: List[Point]


class SolutionBruteForce:
    """
    暴力搜索

    执行用时： 1684 ms , 在所有 Python3 提交中击败了 72.40% 的用户
    内存消耗： 16.5 MB , 在所有 Python3 提交中击败了 5.15% 的用户
    """

    def __init__(self, map_: Map, cycles: List[Cycle]):
        self.map_ = map_
        self.cycles = cycles

    def get_result(self):
        results = []
        for cycle in self.cycles:
            results.append(
                self.get_include_point_cnt(cycle)
            )
        return results

    def get_include_point_cnt(self, cycle):
        result = 0
        for point in self.map_.points:
            if cycle.contain(point):
                result += 1
        return result


class Solution:
    """
    适配leetcode
    """

    def countPoints(self, points: List[List[int]], queries: List[List[int]]):
        solution = SolutionBruteForce(
            map_=Map(
                points=[
                    Point(*point)
                    for point in points
                ],
            ),
            cycles=[
                Cycle(*point)
                for point in queries
            ],
        )
        return solution.get_result()
