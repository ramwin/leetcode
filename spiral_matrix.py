"""
Given an m x n matrix, return all elements of the matrix in spiral order.


written by kimi

example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List


class Solution:
    """
    第一版: 4个append
    第二版: 提示后优化了上下2行的append
    """
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        result = []
        
        while top <= bottom and left <= right:
            # 从左到右遍历上边
            result.extend(matrix[top][left:right + 1])
            top += 1
            
            # 从上到下遍历右边（列无法直接 slice，循环 append）
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # 从右到左遍历下边
            if top <= bottom:
                result.extend(matrix[bottom][left:right + 1][::-1])
                bottom -= 1
            
            # 从下到上遍历左边（列无法直接 slice，循环 append）
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result
