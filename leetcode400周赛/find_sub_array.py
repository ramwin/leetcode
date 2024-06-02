#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from decimal import Decimal
from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def minimumDifference1(self, nums: List[int], start_index, end_index, k: int) -> int:
        """
        i是左下标
        j是右下标
        每次j+1
        """
        """
        1: [1, 2, 3, 4]
        2: [2, 3, 4]
        3: [3, 4]
        """
        min_value = abs(nums[0] - k)
        for i in range(start_index, end_index):
            # print("第一个数字是", nums[i])
            result = nums[i]
            min_value = min(min_value, abs(result-k))
            for j in nums[i+1:end_index]:
                result &= j
                if result == 0:
                    min_value = min(min_value, abs(result - k))
                    break
                if result < k and (k - result) >= min_value:
                    break
                # print(" 求&", j, "得到", result)
                min_value = min(min_value, abs(result - k))
            # print("当前最小是: ", min_value)
        return min_value

    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        k-1, , ,, k , k+12, k+3, ..., k-1,
        a, b, c, d, e, f
        """
        split = [0]
        for index, num in enumerate(nums):
            if num < k:
                split.append(index)
        split.append(len(nums))
        min_value = Decimal("inf")
        # print(split)
        for index, split_index in enumerate(split[:-1]):
            # print("找到", index, split_index)
            min_value = min(self.minimumDifference1(nums, split_index, split[index + 1], k), min_value)
        return min_value
