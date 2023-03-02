#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


improt
"""
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

nums.length == n
nums[i] 是 正整数 ，其中 0 <= i < n
abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
nums 中所有元素之和不超过 maxSum
nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。

注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import math


class Solution1:
    """
    index位置处肯定最大. 然后左右依次 -1, -2
    所以从n和index能算出最多能减多少minus
    最后 maxSum + minus / n 即可
    """

    def __init__(self, n, index, maxSum):
        """"""
        self.n = n
        self.index = index
        self.max = maxSum

    def get_max(self):
        minus = self.get_minus()
        return (self.max + minus) // self.n

    def get_minus(self):
        left_cnt = self.index
        right_cnt = self.n - self.index - 1
        return left_cnt * (left_cnt + 1) // 2 + \
            right_cnt * (right_cnt + 1) // 2


class Solution2:
    """
    index位置处肯定最大. 然后左右依次 -1, -2
    所以从n和index能算出最多能减多少minus
    最后 maxSum + minus / n 即可
    还要注意,不能都减少到0
    """

    def __init__(self, n, index, maxSum):
        """"""
        self.n = n
        self.index = index
        self.max = maxSum

    def get_max(self):
        minus = self.get_minus()
        value = (self.max + minus) // self.n  # 允许减少到0以下的情况
        left_cnt = self.index
        right_cnt = self.n - self.index - 1
        while True:
            left_sum = (value + (value-left_cnt) ) * left_cnt // 2
            right_sum = (value + value - right_cnt) * right_cnt // 2

    def get_minus(self):
        left_cnt = self.index
        right_cnt = self.n - self.index - 1
        return left_cnt * (left_cnt + 1) // 2 + \
            right_cnt * (right_cnt + 1) // 2


class Solution:
    """兼容题目"""
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        return Solution1(n, index, maxSum).get_max()


assert Solution().maxValue(8, 7, 14) == 4
