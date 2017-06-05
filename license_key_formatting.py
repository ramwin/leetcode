#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-06-05 15:21:01


import unittest


# https://leetcode.com/submissions/detail/105023345/
import math
class Solution(object):

    def licenseKeyFormatting(self, S, K):
        key = S.replace('-','').upper()
        length = len(key)
        print('key: %s' % key)
        offset = length % K
        result = key[0:offset]
        print("result: %s" % result)
        pieces = int(math.ceil(length/K))  # I have to add int because the leetcode says range cannot accept a float
        for i in range(0, pieces):
            result += '-' + key[K*i+offset:K*(i+1)+offset]
            print("result: %s" % result)
        return result.strip('-')


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        a = Solution()
        self.assertEqual(a.licenseKeyFormatting('2-4A0r7-4k', 4), '24A0-R74K')
        self.assertEqual(a.licenseKeyFormatting('2-4A0r7-4k', 3), "24-A0R-74K")


if __name__ == '__main__':
    unittest.main()
