#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

"""
绝对差不超过限制的最长连续子数组的单元测试
"""

import logging
import unittest

from absolute import Solution, rm


LOGGER = logging.getLogger("absolute")
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(logging.StreamHandler())


class Test(unittest.TestCase):
    """测试Solution"""

    def test_base(self):
        """测试基础功能"""
        solution = Solution(
            nums=[8, 2, 4, 7], limit=4
        )
        solution.insert_number(solution.nums[0])
        self.assertEqual(
            solution.minimum,
            [4]
        )
        self.assertEqual(
            solution.maximum,
            [12],
        )
        self.assertEqual(
            solution.get_maximum_index(4),
            0,
        )
        self.assertEqual(
            solution.get_maximum_index(3),
            0,
        )
        self.assertEqual(
            solution.get_maximum_index(12),
            0,
        )
        self.assertEqual(
            solution.get_maximum_index(13),
            1,
        )
        self.assertEqual(
            solution.maximum,
            [12],
        )
        self.assertEqual(
            solution.maximum_dict,
            {
                12: {solution.nums[0]},
            }
        )
        self.assertEqual(
            solution.minimum_dict,
            {
                4: {solution.nums[0]},
            }
        )
        self.assertEqual(
            solution.get_minimu_index(4),
            1
        )
        self.assertEqual(
            solution.get_minimu_index(3),
            0
        )
        solution.inspect_number(solution.nums[1])
        solution.insert_number(solution.nums[1])
        self.assertEqual(
            solution.minimum_dict,
            {
                -2: {solution.nums[1]},
            }
        )
        self.assertEqual(
            solution.maximum_dict,
            {
                6: {solution.nums[1]},
            }
        )
        self.assertEqual(
            solution.minimum,
            [-2],
        )

    def test_solution(self):
        """完整测试"""
        solution = Solution(
            nums=[8, 2, 4, 7], limit=4
        )
        solution.inspect_number(solution.nums[0])
        solution.insert_number(solution.nums[0])
        solution.inspect_number(solution.nums[1])
        solution.insert_number(solution.nums[1])

        # 第二步, 2走进来. 8出去
        self.assertEqual(
            solution.minimum,
            [-2],
        )
        self.assertEqual(
            solution.maximum,
            [6],
        )
        self.assertEqual(
            solution.minimum_dict,
            {
                -2: {solution.nums[1]},
            }
        )
        self.assertEqual(
            solution.maximum_dict,
            {
                6: {solution.nums[1]},
            }
        )
        LOGGER.debug("4走进来")
        LOGGER.debug("=======认真开始看=========")
        self.assertEqual(
            solution.maximum_dict,
            {
                6: {solution.nums[1]},
            }
        )
        self.assertEqual(
            solution.maximum,
            [6]
        )
        self.assertEqual(
            solution.get_maximum_index(
                4,
            ),
            0
        )
        solution.inspect_number(solution.nums[2])
        self.assertEqual(
            solution.maximum_dict,
            {
                6: {solution.nums[1]},
            }
        )
        self.assertEqual(
            solution.minimum,
            [-2],
        )
        solution.insert_number(solution.nums[2])
        self.assertEqual(
            solution.minimum,
            [-2, 0],
        )
        self.assertEqual(
            solution.maximum,
            [6, 8],
        )

    def test_solution2(self):
        """测试用例2"""
        solution = Solution(
            nums = [10, 1, 2, 4, 7, 2],  limit = 5
        )
        self.assertEqual(
            solution.get_result(),
            4,
        )

    def test_solution3(self):
        """测试用例3"""
        solution = Solution(
            nums = [4, 2, 2, 2, 4, 4, 2, 2],  limit = 0
        )
        self.assertEqual(
            solution.get_result(),
            3,
        )

    def test_solution4(self):
        """测试用例4"""
        solution = Solution(
            nums = [6, 10, 5, 6],  limit=4,
        )
        self.assertEqual(
            solution.get_result(),
            2
        )
        for i in range(0, 3):
            solution.inspect_number(solution.nums[i])
            solution.insert_number(solution.nums[i])
        # 6, 10, 5依次进入


class UtilsTest(unittest.TestCase):
    """测试所有工具类函数"""

    def test_rm(self):
        """测试rm"""
        a = [4, 5, 6]
        rm(a, 5)
        self.assertEqual(
            a,
            [4, 6]
        )
        rm(a, 4)
        self.assertEqual(
            a,
            [6]
        )
