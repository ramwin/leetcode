#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import unittest

from find_largest_sub_array import Solution


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(Solution().maximumLength([1,1], 2), 2)
        self.assertEqual(Solution().maximumLength([1, 0, 1], 2), 3)
        self.assertEqual(Solution().maximumLength([1,2,3,4,5], 2), 5)
        self.assertEqual(Solution().maximumLength([1,1,2,3,4,5, 5], 2), 5)
        self.assertEqual(Solution().maximumLength([1,1,2,3,4,5, 5], 5), 2)
        self.assertEqual(Solution().maximumLength([1,3,2,3,2,5, 5], 5), 4)
        self.assertEqual(Solution().maximumLength([0,0,0,1,3,2,3,2,5, 5, 0,0,0], 5), 5)
        self.assertEqual(Solution().maximumLength([0,0,0,0,0,0,5,3,2,3,2,5, 5, 0,1,0], 5), 7)
        self.assertEqual(Solution().maximumLength([1,4,2,3,1,4], 3), 3)
