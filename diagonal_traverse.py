#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-04-20 18:06:40


class Solution(object):

    def findDiagonalOrder(self, matrix):
        results = []
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        if len(matrix) == 1:
            return matrix[0]
        direction = 'right_up'
        position_row = 0
        position_column = 0
        results.append(matrix[position_row][position_column])
        import ipdb
        ipdb.set_trace()
        while position_row <= m-1 or position_column <= n-1:
            if direction == 'right_up':
                position_row -= 1
                position_column += 1
                if position_row == -1 and position_column < n:  # 上边界,非最右边
                    position_row = 0
                    direction = 'left_down'
                if position_row == -1 and position_column == n:
                    position_row = 1
                    position_column = n-1
                    direction = 'left_down'
                if position_column == n: # 右边界, 往下走，掉头
                    position_row -= 2
                    position_column -= 1 
                    direction = 'left_down'
            elif direction == 'left_down':
                position_row += 1
                position_column -= 1
                if position_column == -1: # 左边界，往右走，掉头
                    position_column += 1
                    direction = 'right_up'
                    if position_row == m: # 恰好右下角
                        position_row -= 1
                        position_column += 1
                if position_row == m: # 下边界，
                    position_row -= 1
                    position_column += 2
            results.append(matrix[position_row][position_column])
            print(results)
            if position_row == m-1 and position_column == n-1:
                break

        return results
        return [1,2,4,7,5,3,6,8,9]


import unittest

class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution()
        matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ]
        # self.assertEqual(s.findDiagonalOrder(matrix), [1,2,4,7,5,3,6,8,9])
        # self.assertEqual(s.findDiagonalOrder([[1,]]), [1])
        matrix3 = [
            [2,5], [8,4], [0,-1]
        ]
        self.assertEqual(s.findDiagonalOrder(matrix3), [2, 5, 8, 0, 4, -1])


if __name__ == '__main__':
    unittest.main()
