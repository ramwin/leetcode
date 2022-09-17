#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

"""单元测试"""

import unittest

from 水域大小 import Solution1


class Test(unittest.TestCase):
    """测试"""

    def setUp(self):
        """输入和输出配置"""
        self.maps = [
          [0, 2, 1, 0],
          [0, 1, 0, 1],
          [1, 1, 0, 1],
          [0, 1, 0, 1],
        ]
        self.expect_output = [1, 2, 4]

    def test(self):
        """测试"""
        self.assertEqual(
            Solution1(self.maps).get_pools_size(),
            self.expect_output,
        )
