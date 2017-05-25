#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-25 10:20:40


# https://leetcode.com/problems/continuous-subarray-sum/#/description


import unittest


# TODO 从后往前推测，使用动态规划解决呢？

class Solution(object):

    def checkSubarraySum(self, nums, k):
        if k == 0:
            result = False
            for num in nums:
                if num == 0:
                    if result == True:
                        return True
                    result = True
                else:
                    result = False
            return False
        if len(nums) < 2:
            return False
        if len(nums) == 2:
            print("正好2个元素")
            return ((nums[0] + nums[1]) % k) == 0
        start = 0
        total = nums[0]
        posible = set()
        for i in range(1, len(nums)):
            print("当前数字: %d" % nums[i])
            posible = set(map(lambda x: (x+nums[i]) % k, posible))  # 这一步太慢了，结果可能是 k * len(nums) 次操作
            posible.add((nums[i] + nums[i-1])%k)
            print(posible)
            if 0 in posible:
                return True
        return False


class TestS(unittest.TestCase):

    def testsolution(self):
        a = Solution()
        # self.assertEqual(a.checkSubarraySum([23,2,4,6,7], 6), True)
        # self.assertEqual(a.checkSubarraySum([23,2,6,4,7], 6), True)
        # self.assertEqual(a.checkSubarraySum([23,2,6,4,7], 0), False)
        # self.assertEqual(a.checkSubarraySum([0,0], 0), True)
        self.assertEqual(a.checkSubarraySum([1,1], 2), True)


if __name__ == '__main__':
    unittest.main()
