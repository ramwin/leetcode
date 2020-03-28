#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-15 14:18:18



'''
0   1   2   3  ..                 n-1
A0, A1, A2, A3... Ak Ak+1 Ak+2... An-1
1    0  1  0


思路:
Ao - 0  - x
A1 - 1  - x
A2 - 2  - x
...

Ak - k + x
Ak+1 - (k+1) + x


An-1 - (n-1)

B0, B1, B2, B3, ... Bn-1
B0, B1,x=2,  B2, B3, ... Bn-1
B0, B1, B2, x=3, B3, ... Bn-1
x: [
    0: +1_cnt -1_cnt
    1: +1_cnt -1_cnt
]
O(x有n种， 每种x要遍历数组n) = nxn


优化
当x > 某个值时，x后面有一些元素是必定没有Point的
当x > 某个值时，x前面必定有些元素是有point的

# 思路三
每个元素单独当作一个对象。
X列表  x1 x2 x3 x4 x5 x6
元素a: --------- ++++++++
元素b: ---- ++++++ ------
元素c: +++++++++++ ------
元素求出x边界，有n个x

# 思路四
x1--------x2 a+1, b-1---------x3 c+1-----------x4 b+1 ------------- ------------ ----------
每个元素找到自己的链表中的位置，并打点。经过这个点后，数值会因为达到这个元素的边界条件而增减 n 次
循环整个链表，找到最大值。 2n次计算和比较
O(n)
'''

class Solution(object):
    def bestRotation(self, A):
        self.A = A
        self.B = self.get_b_array()  # 保存了元素减去索引的值
        self.n = len(A)
        return self.get_smallest_rotaion()

    def get_smallest_rotaion(self):
        max_point  = 0
        max_x = 0
        for x in range(0, self.n):
            current_point = self.get_x(x)
            if current_point > max_point:
                max_x = x
                max_point = current_point
        return max_x

    def get_b_array(self):
        B_array = []
        for  index, item  in enumerate(self.A):
            B_array.append(
                item -index
            )
        return B_array

    def get_x(self, x):
        """
        index从x开始，每个元素的索引会减去x, 每个元素的值会加上x.
        index小于等于x的值，每个元素的索引会加上 n-x, 所以每个元素会减去 n-x 但是有x个元素可以因为而增加
        """
        count = 0
        for i in range(0, x):
            
            if self.B[i] - (self.n-x) <= 0:
                count += 1
        for j in range(x, self.n):
            if self.B[j] + x <= 0:
                count += 1
        return count



solution = Solution()
solution.bestRotation([2, 3, 1, 4, 0])
b_array = solution.get_b_array()
assert b_array == [2, 2, -1, 1, -4]
# x=1 [-2, 3, 0, 2, -3]
assert solution.get_x(0) == 2
assert solution.get_x(1) == 3
# x=2 [-1, -1, 1, 3, -2]
assert solution.get_x(2) == 3
# x=3 [
assert solution.get_x(3) == 4
assert solution.get_x(4) == 3
assert solution.get_smallest_rotaion()==3
