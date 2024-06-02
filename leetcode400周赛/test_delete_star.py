#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import unittest

from delete_star import Solution


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(
            Solution().clearStars(""),
            "",
        )

    def test1(self):
        self.assertEqual(
            Solution().clearStars("aa**"),
            "",
        )
        self.assertEqual(
            Solution().clearStars("a*a*"),
            "",
        )
        self.assertEqual(
            Solution().clearStars("aaba*"),
            "aab",
        )
        self.assertEqual(
            Solution().clearStars("abc*"),
            "bc",
        )
        self.assertEqual(
            Solution().clearStars("eda*"),
            "ed",
        )

    def test2(self):
        self.assertEqual(
            Solution().clearStars("aaba*"),
            "aab",
        )
