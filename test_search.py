#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""测试旋转数组"""


import unittest
from search_rotate_array_lcci import Ring


class Test(unittest.TestCase):
    """测试"""

    def test1(self):
        """测试ring"""
        ring = Ring([1, 1])
        self.assertEqual(
            ring.min_index,
            0
        )
        ring = Ring([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14])
        self.assertEqual(
            ring.get_index(5),
            8
        )
        ring = Ring([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14])
        self.assertEqual(
            ring.get_index(11),
            -1
        )

    def test_min_index(self):
        ring = Ring([1, 1, 2, 1])
        self.assertEqual(
            ring.min_index,
            3,
        )

    def test_all(self):
        ring = Ring([-47, -42, -42, -42, -39, -36, -35, -33, -33, -32, -31, -28, -27, -26, -25, -24, -24, -19, -14, -7, -3, 1, 8, 8, 13, 14, 14, 15, 16, 17, 19, 21, 24, 25, 27, 28, 32, 33, 36, 39, 39, 43, 46, 46, 49, 55, 56, 58, 62, 63, 64, -62, -62, -60, -60, -58, -58, -57, -57, -53, -52, -51, -51, -47])
        self.assertEqual(
            ring.get_index(644986612),
            -1,
        )
