#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。


示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12
"""


from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        动态规划：原地修改 grid 作为 dp 数组
        dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # 初始化第一行：只能从左边过来
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        
        # 初始化第一列：只能从上面过来
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        
        # 填充其余位置
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[m - 1][n - 1]


import heapq


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Dijkstra 算法：只能向右或向下移动
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # 距离数组，初始化为无穷大
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        
        # 优先队列: (当前距离, 行, 列)
        pq = [(grid[0][0], 0, 0)]
        
        # 方向：只能下、右
        directions = [(1, 0), (0, 1)]
        
        while pq:
            d, i, j = heapq.heappop(pq)
            
            # 如果已经到达终点，直接返回
            if i == m - 1 and j == n - 1:
                return d
            
            # 如果当前距离大于已知最短距离，跳过
            if d > dist[i][j]:
                continue
            
            # 遍历两个方向的邻居（只能下、右）
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    new_dist = d + grid[ni][nj]
                    if new_dist < dist[ni][nj]:
                        dist[ni][nj] = new_dist
                        heapq.heappush(pq, (new_dist, ni, nj))
        
        return dist[m - 1][n - 1]


# 测试代码
if __name__ == "__main__":
    import copy
    
    # 测试用例 1
    grid1 = [[1,3,1],[1,5,1],[4,2,1]]
    print(f"输入: grid = {grid1}")
    
    solution1 = Solution()
    result1_dp = solution1.minPathSum(copy.deepcopy(grid1))
    print(f"Solution (DP) 输出: {result1_dp}")
    
    solution2 = Solution2()
    result1_dijkstra = solution2.minPathSum(copy.deepcopy(grid1))
    print(f"Solution2 (Dijkstra) 输出: {result1_dijkstra}")
    print(f"预期: 7")
    print()
    
    # 测试用例 2
    grid2 = [[1,2,3],[4,5,6]]
    print(f"输入: grid = {grid2}")
    
    result2_dp = solution1.minPathSum(copy.deepcopy(grid2))
    print(f"Solution (DP) 输出: {result2_dp}")
    
    result2_dijkstra = solution2.minPathSum(copy.deepcopy(grid2))
    print(f"Solution2 (Dijkstra) 输出: {result2_dijkstra}")
    print(f"预期: 12")
