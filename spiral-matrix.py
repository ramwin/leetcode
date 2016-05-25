#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-24 11:33:36

# Question
# https://leetcode.com/problems/spiral-matrix/

class Solution(object):

    def spiralOrder2(self, matrix):
        ''' 耗时: 48ms'''
        result = []
        up = 0
        left = 0
        right = 0
        down = 0
        try:
            m = len(matrix) # 行数
            n = len(matrix[0])  # 列数
        except:
            return []
        while up + down < m and right + left < n:
            print('上')
            print(left)
            # print(m-right)
            # print(matrix[up][left:n-right])
            result += matrix[up][left:n-right]
            up += 1
            print(result)
            # 最后一列
            if up + down < m and right + left < n:
                for i in range(up, m-down):
                    print('右')
                    result.append(matrix[i][n-right-1])
                right += 1
                print(result)
            # 最后一行
            if up + down < m and right + left < n:
                print(right)
                print(left)
                for i in range(n-right-1, left-1, -1):
                    print('下')
                    result.append(matrix[m-down-1][i])
                down += 1
            print(result)
            # 第一列
            if up + down < m and right + left < n:
                for i in range(m-down-1, up-1, -1):
                    print('左')
                    result.append(matrix[i][left])
                left += 1
        return result
        

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        耗时:   64ms
        """
        self.matrix = matrix
        self.result = []
        self.result += self.matrix.pop(0)
        while self.matrix:
            self.invert()
            self.result += self.matrix.pop(0)
        return self.result

    def invert(self):
        print(self.matrix)
        self.tmp_out = []
        for column in range(len(self.matrix[0])-1, -1, -1):
            self.tmp_in = []
            for line in range(len(self.matrix)):
                print('%d, %d' % (line, column))
                self.tmp_in.append(self.matrix[line][column])
            self.tmp_out.append(self.tmp_in)
        self.matrix = self.tmp_out

a = Solution()
print(a.spiralOrder2([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

