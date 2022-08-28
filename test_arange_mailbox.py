#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>
"""
测试安排邮箱
"""

import logging
from unittest import TestCase
from arange_mailbox import HouseList, MySolution as Solution

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


class HouseTest(TestCase):
    """测试房子列表"""

    def test_iter_start_end(self):
        """测试iter_start_end"""
        house_list = HouseList([1, 4])
        self.assertEqual(list(house_list.iter_start_end(0, 2)), [
            [0, 1],
        ])
        house_list = HouseList([1, 4, 9])
        self.assertEqual(list(house_list.iter_start_end(0, 2)), [
            [0, 1],
        ])
        house_list = HouseList([1, 2, 3, 4])
        self.assertEqual(list(house_list.iter_start_end(1, 3)), [
            [1, 2],
        ])

    def test_get_total_distance(self):
        """测试get_total_distance"""
        house_list = HouseList([1, 4])
        self.assertEqual(house_list.get_total_distance(0, 1), 0)
        self.assertEqual(house_list.get_total_distance(0, 2), 3)


class SolutionTest(TestCase):
    """测试Solution"""

    def test_get_result1(self):
        """最简单的测试"""
        self.assertEqual(Solution([1, 4], 2).get_result(0, 2, 2), 0)
        self.assertEqual(Solution([1, 4, 8], 2).get_result(0, 3, 2), 3)

    def test_get_result2(self):
        """测试get_result"""
        houses = [1, 4, 8, 10, 20]
        house_list = HouseList(houses)
        self.assertEqual(list(house_list.iter_start_end(0, 3)), [
            [0, 1],
            [1, 2],
        ])
        solution = Solution(houses, 3)
        logger.info(solution.house_list)
        self.assertEqual(solution.get_result(0, 3, 2), 3)

    def test_get_result3(self):
        """测试get_result"""
        self.assertEqual(Solution([1, 4, 8], 2).get_result(0, 3, 2), 3)

    def test_get_result4(self):
        """测试get_result"""
        self.assertEqual(Solution([1, 4, 8, 10, 20], 3).get_result(0, 5, 3), 5)
        self.assertEqual(Solution([2, 3, 5, 12, 18], 2).get_result(0, 5, 2), 9)
        self.assertEqual(Solution([7, 4, 6, 1], 1).get_result(0, 4, 1), 8)
        self.assertEqual(Solution([3, 6, 14, 10], 4).get_result(0, 4, 4), 0)


class SpeedTest(TestCase):
    """测试性能数据"""

    def test(self):
        """最大的结果"""
        houses = [
            427, 498, 461, 44, 240, 273, 12, 413, 61, 441, 353, 261, 92, 112,
            445, 430, 375, 443, 76, 233, 311, 285, 378, 369, 279, 55, 202, 124,
            468, 406, 478, 417, 409, 253, 429, 34, 348, 487, 454, 463, 102,
            131, 35, 190, 383, 239
        ]
        k = 23
        self.assertEqual(
            Solution(houses, k).get_result(0, len(houses), k), 110)
