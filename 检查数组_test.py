#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""检查数组对的测试用例"""


import unittest

from check_arr import Solution5


class Test(unittest.TestCase):
    """基础测试"""

    def test1(self):
        """leetcode第一次错误,取余为0"""
        arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
        k = 5
        self.assertTrue(
            Solution5(arr, k).check()
        )

    def test2(self):
        """leetcode第二次错误,复数"""
        arr = [-4, -7, 5, 2, 9, 1, 10, 4, -8, -3]
        k = 3
        self.assertTrue(
            Solution5(arr, k).check()
        )

    def test3(self):
        """leetcode第三次错误"""
        arr = [39, 5, 30, -8, 46, 1, -10, 10, 8, -6, -5, 10]
        k = 40
        self.assertTrue(
            Solution5(arr, k).check()
        )

    def test4(self):
        """leetcode第四次错误"""
        arr = [2, 3, 7, -9, 4, 4, 7, 3, 2, 10, 8, 15, 2, 1, -8, 10, -5, 10, -2, 21, 9, 20, 0, 4, 24, 5, 12, -10, 8, 9, 18, 13, -8, 10, -4, -3, 0, 16, -4, 8, 14, 15, -9, 0, 0, -6, 11, -3, 10, 11, 7, -1, -5, 5, 11, 2, 5, 9, -2, 8, 9, -10, 6, -2, 7, 8, 3, 0, -2, 11]
        k = 18
        self.assertTrue(
            Solution5(arr, k).check()
        )
