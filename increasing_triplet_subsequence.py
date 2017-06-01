#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-06-01 11:56:13


# https://leetcode.com/problems/increasing-triplet-subsequence/#/description


import unittest


class Solution(object):

    def increasingTriplet(self, nums):
        if nums == []:
            return False
        minium = nums[0]  # the minisy
        middle_num = None
        for num in nums:
            if num < minium:
                minium = num
            if num > minium:
                if middle_num is None:
                    middle_num = num
                elif num < middle_num:
                    middle_num = num
                elif num > middle_num:
                    return True
        return False


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        a = Solution()
        self.assertEqual(a.increasingTriplet([1,2,3,4,5]), True)
        self.assertEqual(a.increasingTriplet([5,4,3,2,1]), False)


if __name__ == '__main__':
    unittest.main()
