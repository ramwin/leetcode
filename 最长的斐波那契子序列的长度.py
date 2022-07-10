#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from typing import List

# 上次提交
# 执行用时： 4124 ms , 在所有 Python3 提交中击败了 7.86% 的用户
# 内存消耗： 15.5 MB , 在所有 Python3 提交中击败了 72.48% 的用户

# 添加 start_0 * 2 ** ()的判断后
# 执行用时： 3744 ms , 在所有 Python3 提交中击败了 10.81% 的用户
# 内存消耗： 15.5 MB , 在所有 Python3 提交中击败了 71.99% 的用户

# 删除calculated相关代码的话
# 执行用时： 2888 ms , 在所有 Python3 提交中击败了 21.41% 的用户
# 内存消耗： 15 MB , 在所有 Python3 提交中击败了 92.92% 的用户


class RealSolution:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.nums = set(arr)
        self.arr = arr
        self.calculated = set()  # (pre, next)

    def longest(self) -> int:
        longest = 0
        current_long = 0
        for start_0_index in range(0, len(self.arr)):
            for start_1_index in range(start_0_index + 1, len(self.arr)):
                start_0 = self.arr[start_0_index]
                if start_0 * 2 ** (longest // 2 - 1) >= self.arr[-1]:
                    if longest >= 3:
                        return longest
                    return 0
                start_1 = self.arr[start_1_index]
                # if (start_0, start_1) in self.calculated:
                #     continue
                current_long = self.get_length(start_0, start_1)
                if current_long > longest:
                    longest = current_long
        if longest >= 3:
            return longest
        else:
            return 0

    def get_length(self, prev, _next) -> int:
        result = 2
        while True:
            if prev + _next in self.nums:
                result += 1
                prev, _next = _next, prev + _next
                # self.calculated.add(
                #     (prev, _next)
                # )
                continue
            break
        return result


class Solution:

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        return RealSolution(arr).longest()
