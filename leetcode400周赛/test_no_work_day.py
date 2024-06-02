#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import unittest

from no_work_day import Solution


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(
                Solution().countDays(10,  [[5,7],[1,3],[9,10]]),
                2,
        )
        self.assertEqual(
                Solution().countDays(6,  [[1, 6]]),
                0,
        )
        self.assertEqual(
                Solution().countDays(5,  [[2, 4], [1, 3]]),
                1,
        )
        self.assertEqual(
                Solution().countDays(5,  []),
                5,
        )
        self.assertEqual(
                Solution().countDays(5,  [[1, 3]]),
                2,
        )
        self.assertEqual(
                Solution().countDays(5,  [[1, 3], [4, 5]]),
                0,
        )
