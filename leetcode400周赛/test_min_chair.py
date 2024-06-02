#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import unittest
from min_chair import Solution


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(
                Solution().minimumChairs("EEEEEEE"), 7
        )
        self.assertEqual(
                Solution().minimumChairs("ELELEEL"), 2
        )
        self.assertEqual(
                Solution().minimumChairs("EE"), 2
        )
        self.assertEqual(
                Solution().minimumChairs(""), 0
        )
