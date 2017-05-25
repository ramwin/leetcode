#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-24 16:42:05

import unittest


class Solution(object):
    def matrixReshape(self, nums, r, c):
        if len(nums) == 0:  # nums = []
            if c == 0:
                return [[]] * r
            else:
                return []
        if len(nums[0]) == 0:
            if c == 0:
                return [[]] * r
            else:
                return []
        if len(nums) * len(nums[0]) != r * c:
            return nums

        num_rows = len(nums)
        num_columns = len(nums[0])
        results = []
        row_start = -1
        column_start = -1
        for row in range(r):
            # print("正在生成矩阵第{0}行".format(row))
            tmp = []
            for column in range(c):
                # print("正在生成举证第{0}列".format(column))
                column_start = (column_start + 1) % num_columns
                if column_start == 0:
                    row_start += 1
                # print("正在读取原来举证的第{0}行第{1}列".format(row_start, column_start))
                tmp.append(nums[row_start][column_start])
            results.append(tmp)
        return results



class Test(unittest.TestCase):
    def testsolution(self):
        print('1')
        a = Solution()
        nums = [[1,2],[3,4]]
        self.assertEqual(a.matrixReshape(nums, 1, 4),[[1,2,3,4]])
        nums = [[1.2],[3,4]]
        self.assertEqual(a.matrixReshape(nums, 2, 4),[[1.2],[3,4]])


if __name__ == '__main__':
    unittest.main()
