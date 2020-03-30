#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2020-03-30 10:23:19


"""
题目链接: https://leetcode.com/problems/combination-sum/
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution:
    def combinationSum(self, candidates, target: int):
        candidates.sort()
        self.candidates = candidates
        self.max_index = len(candidates) - 1
        self.max_value = candidates[-1]
        # XXX
        for (index, value) in enumerate(self.candidates):
            if value > target:
                self.max_index = index
                break
        return self.get_solution_list(0, target)

    def get_solution_list(self, index, target):
        # 只从index开始的candidates，生成target的list
        # 有第index元素
        # print(f"get_solution_list: index={index}, target={target}")
        if target < 0:
            return []
        if target == 0:
            return [[]]
        if index > self.max_index:
            return []
        if index == self.max_index:
            if target % self.candidates[index] == 0:
                result = [[self.candidates[index], ]*(target//self.candidates[index])]
                return result
            else:
                return []
        result = []
        first_value = self.candidates[index]
        for i in range(target//first_value+1):
            first_list = [first_value] * i
            for j in self.get_solution_list(index+1, target-i*self.candidates[index]):
                result.append(first_list + j)
        return result


solution = Solution()
# print(solution.combinationSum([2,3,6,7], 7))
# print(solution.combinationSum([2,3,5], 8))
print(solution.combinationSum([1], 2))
