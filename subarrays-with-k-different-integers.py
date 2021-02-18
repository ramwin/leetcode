#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-18 11:19:45


# Question
# https://leetcode-cn.com/problems/subarrays-with-k-different-integers/

"""
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarrays-with-k-different-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, A, K) -> int:
        self.A = A
        print(self.A)
        self.element_dict = defaultdict(int)
        self.start_index = 0
        self.end_index = K
        self.solutions = 0
        self.k = K
        for i in A[self.start_index: self.end_index]:
            self.element_dict[i] += 1

        while len(self.element_dict) < self.k:
            self.element_dict[self.A[self.end_index]] += 1
            self.end_index += 1

        self.solutions += 1
        print(f"第{self.solutions}次找到: {self.element_dict}, start_index: {self.start_index}, end_index: {self.end_index}")

        while self.find_next_solution():
            pass
        return self.solutions

    def find_next_solution(self):
        print("find_next_solution")
        self.end_index += 1
        self.element_dict[A[self.end_index-1]] += 1
        while len(self.element_dict) > self.k:
            print("哟吼, 超过啦")
            print(self)
            self.start_index += 1
            print(f"self.start_index继续加1: {self.start_index}")
            self.element_dict[A[self.start_index-1]] -= 1
            if self.element_dict[self.A[self.start_index-1]] == 0:
                self.element_dict.pop(self.A[self.start_index-1])
        self.solutions += 1
        print(f"找到啦: {self.element_dict}")
        print(f"第{self.solutions}次找到: {self.element_dict}, start_index: {self.start_index}, end_index: {self.end_index}")
        return True

    def __str__(self):
        return f"当前: {self.element_dict}, start_index: {self.start_index}, end_index: {self.end_index}"



for A, K, n in [
    [[1,2,1,2,3], 2, 7],
    # [[1,2,1,3,4], 3, 3],
        ]:
    assert Solution().subarraysWithKDistinct(A, K) == n
