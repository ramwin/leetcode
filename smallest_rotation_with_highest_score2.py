#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-28 16:05:41



"""
对于数字N, 当k转移时，他的位置就变成了原来的索引+k % N
如果 新位置大于数字N的值，说明这个数字就变化了

k: 每个元素的索引增加 length - k
所以k越大（不超过max_index_k)时，元素增加的索引越小，越容易变0, 直到k达到元素的max_index_k, 使得元素变成最后一个元素

k=n 相当于没有人移动
k变小
所以每个元素，当k等于他的索引时，他就惨了, score = 0
但是一旦k继续变小，导致 origin_index - index >= value 时，他就幸福了
"""

class Item(object):

    def __init__(self, origin_index, value, length):
        self.origin_index = origin_index
        self.value = value
        self.length = length

    def zero_to_one_k(self):
        """
        当k为多少时，这个元素开始有score, 因为他到最后面了
        """
        return (self.origin_index + 1) % self.length

    def one_to_zero_k(self):
        """当k达到多少时，会导致元素从1变成0, 因为移动的数量太少了"""
        return (self.origin_index-self.value+self.length+1) % self.length


class Solution(object):

    def bestRotation(self, A):
        lines = [0]* len(A)
        length = len(A)
        for index, value in enumerate(A):
            if value > len(A) - 1:
                # 不管k等于多少，都不可能value <= index
                continue
            if value <= 0:
                # 不管k等于多少，都 value <= index
                continue
            item = Item(index, value, length)
            lines[item.zero_to_one_k()] += 1
            lines[item.one_to_zero_k()] -= 1
            # lines[
            #     (index + 1) % length
            # ] += 1
            # lines[
            #     (index - value + 1) % length
            # ] -= 1
        current_max = lines[0]
        current_max_index = 0
        current = 0
        for index, line in enumerate(lines):
            current += line
            if current > current_max:
                current_max = current
                current_max_index = index
        return current_max_index


solution = Solution()
print(solution.bestRotation([2, 3, 1, 4, 0]))
