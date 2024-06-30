#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from unittest import TestCase

from highest_triangle import Solution


class Test(TestCase):

    def test1(self):
        self.assertEqual(Solution().maxHeightOfTriangle(0, 0), 0)
        self.assertEqual(Solution().maxHeightOfTriangle(1, 0), 1)
        self.assertEqual(Solution().maxHeightOfTriangle(0, 1), 1)
        self.assertEqual(Solution().maxHeightOfTriangle(0, 2), 1)
        self.assertEqual(Solution().maxHeightOfTriangle(2, 4), 3)
        self.assertEqual(Solution().maxHeightOfTriangle(4, 2), 3)
        self.assertEqual(Solution().maxHeightOfTriangle(10, 1), 2)
