#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
https://leetcode.cn/problems/rearrange-spaces-between-words/
重新排列单词间的空格
"""


class Solution1:
    """
    计算有多少个空格n
    有多少个单词m
    那么每个单词中间的空格数 = n // (m-1)
    最尾添加 n % (m-1) 个空格
    执行用时： 44 ms , 在所有 Python3 提交中击败了 36.42% 的用户
    内存消耗： 16.1 MB , 在所有 Python3 提交中击败了 25.83% 的用户
    """

    def __init__(self, text):
        self.text = text
        self.space_cnt = text.count(" ")
        self.words = text.strip().split()

    def get_result(self) -> str:
        gap_cnt = len(self.words) - 1
        if gap_cnt == 0:
            middle_cnt = 0
            end_cnt = self.space_cnt
        else:
            middle_cnt, end_cnt = divmod(
                self.space_cnt,
                gap_cnt
            )
        gap = " " * middle_cnt
        result = gap.join(self.words) + \
            " " * end_cnt
        return result



class Solution:
    """模板"""
    def reorderSpaces(self, text: str) -> str:
        return Solution1(text).get_result()


if __name__ == "__main__":
    test_text = "  this   is  a sentence "
    test_result = Solution().reorderSpaces(test_text)
    print(test_result)
