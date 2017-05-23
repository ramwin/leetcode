#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-23 15:36:25


import unittest


class Solution(object):
    def singleNonDuplicate(self, nums):
        a = 0
        for num in nums:
            a ^= num
        return a


class Test(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.singleNonDuplicate([1,1,2,3,3]), 2)


if __name__ == '__main__':
    unittest.main()
