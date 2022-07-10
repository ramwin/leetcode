#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


# 执行用时： 36 ms , 在所有 Python3 提交中击败了 84.72% 的用户
# 内存消耗： 15 MB , 在所有 Python3 提交中击败了 57.57% 的用户

from typing import List
from collections import defaultdict


class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i in nums1:
            dict1[i] += 1
        for j in nums2:
            dict2[j] += 1
        result = []
        for k in dict1:
            if k in dict2:
                result += [k] * min(dict1[k], dict2[k])
        return result
