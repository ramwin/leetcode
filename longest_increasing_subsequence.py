#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-12-06 14:36:06


# TODO 才写到一半
import unittest


        


class Solution:
    class Storage:
        """
        保存一个列表的各种最大数值各种最小数值下的最长子序列
        """

        def __init__(self, nums):
            if len(nums) == 1:
                self.value_list = nums[0]
                self.value_nequal_dict = {  # 不超过某个数或者不小于某个数的最长自学列的长度 存在key，说明storage里面的最长序列是存在这个key的
                    nums[0]: {
                        "max": {  # 当nums[0]做为最大值的列表
                            "length": 1,
                            "min": num[0],  # 此时列表的最小值
                        },
                        "min":  {  # 当nums[0]作为最小值的列表
                            "length": 1,
                            "max": num[0],  # 此时列表的最大值
                        }
                    }
                }
                return
            self.value_list = []  # [1,2,3,4]
            self.value_dict = {
                # 1: {
                #     "length_as_max": 1,
                #     "length_as_mix": 2,
                # }
            }
            middle_index = len(nums)//2
            left_storage = Storage(nums[0:middle_index])
            right_storage = Storage(nums[middle_index:])
            left_index = right_index = 0
            while True:
                left_value = left_storage.value_list[left_index]
                left_state = left_storage.value_nequal_dict[left_value]
                right_value = right_storage.value_list[right_index]
                right_state = right_storage.value_nequal_dict[right_index]
                if left_value == right_value:
                    # 第一种, 左侧的左侧加上右侧的右侧
                    self.value_dict[
                    ]
                    # 第二种，右侧的左侧加上左侧的右侧
                elif left_value


    def lengthOfLIS(self, nums: List[int]) -> int:




class MyTest(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(
            Solution().lengthOfLIS([10,9,2,5,3,7,101,18], 4),
        )


if __name__ == "__main__":
    unittest.main()
