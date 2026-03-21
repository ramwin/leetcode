#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
给你一个整数数组 nums ，如果 nums 至少 包含 2 个元素，你可以执行以下操作中的 任意 一个：

选择 nums 中最前面两个元素并且删除它们。
选择 nums 中最后两个元素并且删除它们。
选择 nums 中第一个和最后一个元素并且删除它们。
一次操作的 分数 是被删除元素的和。

在确保 所有操作分数相同 的前提下，请你求出 最多 能进行多少次操作。

请你返回按照上述要求 最多 可以进行的操作次数。



示例 1：

输入：nums = [3,2,1,2,3,4]
输出：3
解释：我们执行以下操作：
- 删除前两个元素，分数为 3 + 2 = 5 ，nums = [1,2,3,4] 。
- 删除第一个元素和最后一个元素，分数为 1 + 4 = 5 ，nums = [2,3] 。
- 删除第一个元素和最后一个元素，分数为 2 + 3 = 5 ，nums = [] 。
由于 nums 为空，我们无法继续进行任何操作。
示例 2：

输入：nums = [3,2,6,1,4]
输出：2
解释：我们执行以下操作：
- 删除前两个元素，分数为 3 + 2 = 5 ，nums = [6,1,4] 。
- 删除最后两个元素，分数为 1 + 4 = 5 ，nums = [6] 。
至多进行 2 次操作。

"""

from typing import List
from functools import lru_cache


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        """
        区间 DP：枚举第一次操作的分数，然后计算最多操作次数
        优化：如果前两个和后两个的和相同，只需要计算一次
        """
        n = len(nums)
        if n < 2:
            return 0
        
        # 三种可能的初始分数
        score1 = nums[0] + nums[1]      # 删除前两个
        score2 = nums[-1] + nums[-2]    # 删除后两个
        score3 = nums[0] + nums[-1]     # 删除首尾
        
        # 如果三种分数都相同，直接计算一次即可
        if score1 == score2 == score3:
            return self._solve(nums, score1)
        
        # 否则分别计算不同的分数
        ans = 0
        for score in {score1, score2, score3}:
            ans = max(ans, self._solve(nums, score))
        
        return ans
    
    def _solve(self, nums: List[int], target_score: int) -> int:
        """计算以 target_score 为分数时的最大操作次数"""
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def dfs(l: int, r: int) -> int:
            if r - l + 1 < 2:
                return 0
            
            res = 0
            # 删除前两个
            if l + 1 <= r and nums[l] + nums[l + 1] == target_score:
                res = max(res, 1 + dfs(l + 2, r))
            # 删除后两个
            if r - 1 >= l and nums[r - 1] + nums[r] == target_score:
                res = max(res, 1 + dfs(l, r - 2))
            # 删除首尾
            if nums[l] + nums[r] == target_score:
                res = max(res, 1 + dfs(l + 1, r - 1))
            
            return res
        
        return dfs(0, n - 1)


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例 1
    nums1 = [3, 2, 1, 2, 3, 4]
    print(f"输入: nums = {nums1}")
    print(f"输出: {solution.maxOperations(nums1)}")
    print(f"预期: 3")
    print()
    
    # 测试用例 2
    nums2 = [3, 2, 6, 1, 4]
    print(f"输入: nums = {nums2}")
    print(f"输出: {solution.maxOperations(nums2)}")
    print(f"预期: 2")

