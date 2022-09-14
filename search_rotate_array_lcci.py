#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
https://leetcode.cn/problems/search-rotate-array-lcci/
"""


import bisect


class BruteForceSolution:
    """
    升序排列, 经过N次旋转
    1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25

    暴力搜索
    执行用时： 40 ms , 在所有 Python3 提交中击败了 50.11% 的用户
    内存消耗： 15.8 MB , 在所有 Python3 提交中击败了 77.30% 的用户
    """
    def search(self, arr, target) -> int:
        """暴力搜索"""
        try:
            return arr.index(target)
        except ValueError:
            return -1


def get_min_index(arr):
    """返回arr里面最小元素的索引, 最小的元素必须在[start:end+1]里面"""
    previous = arr[0]
    for index, num in enumerate(arr):
        if num < previous:
            return index
        previous = num
    return 0


class Ring:
    """
    环形数组
    """

    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)  # 环长
        self.min_index = get_min_index(arr)  # 起始位置
        if self.min_index == 0:  # 没有旋转
            self.left_arr = self.arr
            self.right_arr = []
        else:
            self.left_arr = self.arr[0: self.min_index]
            self.right_arr = self.arr[self.min_index:]

    def get_index(self, target):
        """搜索target, 返回索引或者-1"""
        left_index = bisect.bisect_left(self.left_arr, target)
        if self.left_arr and (left_index < len(self.left_arr)) and self.left_arr[left_index] == target:
            return left_index
        right_index = bisect.bisect_left(self.right_arr, target)
        if self.right_arr and (right_index < len(self.right_arr)) and self.right_arr[right_index] == target:
            return right_index + self.min_index
        return -1


class Solution:
    """

    执行用时： 36 ms , 在所有 Python3 提交中击败了 73.88% 的用户
    内存消耗： 16.1 MB , 在所有 Python3 提交中击败了 5.57% 的用户

    我们发现, 这个数组不管旋转多少次, 从环形数组来看, 都是升序的
    1 2 3 4 5
    4 5 1 2 3
    5 1 2 3 4
    2 3 4 5 1

    二分法
    用arr中间的值和第一个值和最后一个值比较

    1. 如果 第一个值 <= 中间的值 <= 最后一个值, 说明数组是升序排列的
        如 1 2 4 5 6
        那直接二分找到target
    2. 第一个值 > 中间的值 > 最后一个值不可能的情况
    3. 如果 第一个值 >= 中间的值 <= 最后一个的值, 说明中间的值到最后一个的值是单调递增的
    4. 如果 第一个值 <= 中间的值 >= 最后一个的值, 说明第一个值到中间的值是单调递增的
    """

    def search(self, arr, target):
        """搜索"""
        return Ring(arr).get_index(target)
