#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
测试同源字符串
"""

import unittest
from same_source import MyString


class TestMyString(unittest.TestCase):
    """测试 MyString"""

    def setUp(self):
        self.string1 = "internationalization"
        self.string2 = "l123e"
        self.string3 = "123"
        self.string4 = "le"
        self.string5 = "l1l2"
        self.string6 = "3l1l"

    def test_string_2_list(self):
        """测试 string_2_list """
        self.assertEqual(
            MyString(self.string2).split_by_letter,
            ["l", "123", "e"]
        )
        self.assertEqual(
            MyString(self.string3).split_by_letter,
            ["123"]
        )
        self.assertEqual(
            MyString(self.string4).split_by_letter,
            ["l", "e"]
        )
        self.assertEqual(
            MyString(self.string5).split_by_letter,
            ["l", "1", "l", "2"]
        )
        self.assertEqual(
            MyString(self.string6).split_by_letter,
            ["3", "l", "1", "l"]
        )
