#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-04-06 10:24:26


class Solution(object):

    def __init__(self, array):
        self.array = array
        print(f"self.array: {array}")

    def get_min_index(self):
        return self.get(0, len(self.array))

    def get(self, start_index, end_index):
        # end_index不包含在内
        print(f"self.get: start_index: {start_index}, end_index: {end_index}")
        if end_index - start_index == 1:
            return 0
        if end_index - start_index == 2:
            if self.array[end_index-1] > self.array[start_index]:
                return start_index-1
            return end_index-1

        half_index = start_index + (end_index - start_index)// 2
        if self.array[half_index] < self.array[half_index-1]:
            print("变了")
            return half_index
        if self.array[half_index] < self.array[start_index]:
            print("在前办部分哦")
            return self.get(start_index, half_index)
        return self.get(half_index, end_index)


solution = Solution(
    [3,4,5,1,2]
)
assert solution.get_min_index() == 3
solution = Solution(
    [2,3,4,5,1]
)
assert solution.get_min_index() == 4
solution = Solution(
    [2,3,4,5]
)
assert solution.get_min_index() == 1
solution = Solution(
    [4,5, 2,3,]
)
assert solution.get_min_index() == 2
