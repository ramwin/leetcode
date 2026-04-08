#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
给你一个长度为 n 的数组 nums1，其中包含 互不相同 的整数。

你需要构造另一个长度为 n 的数组 nums2，使得 nums2 中的元素要么全部为 奇数，要么全部为 偶数。

对于每个下标 i，你必须从以下两种选择中 任选其一（顺序不限）：

nums2[i] = nums1[i]
nums2[i] = nums1[i] - nums1[j]，其中 j != i
如果能够构造出满足条件的数组，则返回 true；否则，返回 false。

©leetcode

只要里面存在>2个的奇数,偶数. 必定可以构造
奇数,奇数(复制),偶数(减去第一个奇数), 必定可以构造

a b c d e f g
"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        self.nums1 = nums1
        can_build_odd = True
        can_build_even = True
        has_odd = False
        has_even = False
        for index, num in enumerate(nums1):
            if (not can_build_even) and (not can_build_odd):
                return False
            if has_odd and has_even:
                return True
            # 碰到奇数并且没有奇数给你减
            if num % 2 == 1:
                if not has_odd:
                    can_build_even = False
                has_odd = True
            # 碰到偶数并且没有奇数给你减
            if num % 2 == 0:
                if not has_odd:
                    can_build_odd = False
                has_even = True
        return can_build_even or can_build_odd
