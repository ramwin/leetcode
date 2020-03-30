#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-30 10:23:19


"""
题目链接: https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        self.candidate_cnt_dict = {}
        for candidate in candidates:
            if candidate > target:
                break
            if candidate not in self.candidate_cnt_dict:
                self.candidate_cnt_dict[candidate] = 1
            else:
                self.candidate_cnt_dict[candidate] += 1
        self.candidates = list(self.candidate_cnt_dict.keys())
        self.max_index = len(self.candidates) - 1
        if not self.candidates:
            return []
        self.max_value = self.candidates[-1]
        # print(f"self.max_index: {self.max_index}")
        # print(f"self.candidates: {self.candidates}")
        return self.get_solution_list(0, target)

    def get_solution_list(self, index, target):
        # 只从index开始的candidates，生成target的list
        # 有第index元素
        # print(f"get_solution_list: index={index}, target={target}")
        result = []
        if target < 0:
            result = []
        elif target == 0:
            result = [[]]
        elif index > self.max_index:
            result = []
        # elif index == self.max_index:
        #     if target == self.candidates[index]:
        #         result = [[target]]
        #     else:
        #         result = []
        else:
            first_value = self.candidates[index]
            # print(f"    first_value: {first_value}的数量有{self.candidate_cnt_dict[first_value]}")
            for i in range(0, self.candidate_cnt_dict[first_value]+1):
                # print(f"    i={i}")
                first_list = [first_value] * i
                _  = self.get_solution_list(index+1, target-i*first_value)
                for j in _:
                    result.append(first_list + j)
        # print(f"get_solution_list: index: {index}, target: {target}, result: {result}")
        return result


solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))
print(solution.combinationSum2([1,1,2], 2))
print(solution.combinationSum2([2], 1))
print(solution.combinationSum2([1, 1], 2))
