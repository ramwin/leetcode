#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-08 16:38:12


from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        results = defaultdict(int)
        for num in nums:
            results[num] += 1
        threshold = len(nums)/3
        l = []
        for key, value in results.items():
            if value > threshold:
                l.append(key)
        return l


# solution using boyer-moore majority
# https://discuss.leetcode.com/topic/17564/boyer-moore-majority-vote-algorithm-and-my-elaboration
class Solution:
# @param {integer[]} nums
# @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]

import unittest

class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        self.assertEqual(s.majorityElement([]), [])
        self.assertEqual(s.majorityElement([1,2,3]), [])
        self.assertEqual(s.majorityElement([2,2,3]), [2])
        self.assertEqual(set(s.majorityElement([1, 2])), set([1, 2]))
        self.assertEqual(set(s.majorityElement([
            1,1,1,1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
        ])), set([1]))


if __name__ == '__main__':
    unittest.main()
