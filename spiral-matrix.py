#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-24 11:33:36

# Question
# https://leetcode.com/problems/spiral-matrix/

class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
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
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

