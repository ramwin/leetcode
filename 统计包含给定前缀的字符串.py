#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>



"""
https://leetcode.cn/problems/counting-words-with-a-given-prefix/submissions/
执行用时： 40 ms , 在所有 Python3 提交中击败了 49.52% 的用户
内存消耗： 15 MB , 在所有 Python3 提交中击败了 74.60% 的用户
"""


from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for word in words:
            if word.startswith(pref):
                result += 1
        return result
