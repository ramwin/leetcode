#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""单元测试"""


import unittest
from 从前序与中序遍历序列构造二叉树 import Solution1


class Test(unittest.TestCase):
    """基础测试"""

    def test1(self):
        solution = Solution1(
            [20, 15, 7],
            [15, 20, 7],
        )

    def test2(self):
        solution = Solution1(
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
        )

    def test3(self):
        """
            1
          2
        3
        """
        solution = Solution1(
            [1, 2, 3],
            [3, 2, 1],
        )
