#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-06-01 11:00:45


from collections import defaultdict
import unittest

# https://leetcode.com/problems/top-k-frequent-elements/#/description


class Solution(object):

    def topKFrequent(self, nums, k):
        cnt_dict = defaultdict(int)
        for num in nums:
            cnt_dict[num] += 1
        result = defaultdict(list)
        for num, cnt in cnt_dict.items():
            result[cnt].append(num)
        # print(cnt_dict)
        cnts = list(set(list(cnt_dict.values())))
        cnts.sort(reverse=True)
        # print(cnts)
        return_list = []
        for i in cnts:
            return_list += result[i]
        return return_list[0:k]



class SolutionTest(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        # self.assertEqual(s.topKFrequent([1,1,1,2,2,3], 2), [1,2])
        # self.assertEqual(s.topKFrequent([1, 2], 2), [1,2])
        self.assertEqual(s.topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10), [1,2,5,3,7,6,4,8,10,11])


if __name__ == '__main__':
    unittest.main()
