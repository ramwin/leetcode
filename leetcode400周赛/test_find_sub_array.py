#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import unittest

from find_sub_array import Solution


class Test(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.minimumDifference([1,2,4,5], 3),
            1
        )
        self.assertEqual(
            solution.minimumDifference([1, 2, 1, 2], 2),
            0
        )
        self.assertEqual(
            solution.minimumDifference([1], 10),
            9
        )
        self.assertEqual(
            solution.minimumDifference([1], 1),
            0
        )

    def test2(self):
        solution = Solution()
        self.assertEqual(
            solution.minimumDifference([5, 13, 90, 92, 49], 10),
            2
        )
        self.assertEqual(
            solution.minimumDifference([41,27,47,8,39], 12),
            1
        )

    def test3(self):
        solution = Solution()
        self.assertEqual(
            solution.minimumDifference([56,46,80,58,56], 1),
            1
        )

    def test4(self):
        solution = Solution()
        self.assertEqual(
            solution.minimumDifference1([6], 0, 1, 2),
            4
        )
        self.assertEqual(
            solution.minimumDifference([6], 2),
            4
        )
