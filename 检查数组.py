#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

"""
https://leetcode.cn/problems/check-if-array-pairs-are-divisible-by-k/
"""

from collections import defaultdict


class Solution1:
    """
    对arr进行循环, 每个数字ni, 获取 i对k的取余remain
    [n0, n1, ... ni-1, ni, ni+1...]
    查看之前是否存在数字的取余是 k - remain
        如果不存在, 就把remain添加到待匹配
        如果存在, 就把 k - remain 移除待匹配
    根据待匹配是否为空, 返回True False

    执行用时： 212 ms , 在所有 Python3 提交中击败了 5.70% 的用户
    内存消耗： 27.9 MB , 在所有 Python3 提交中击败了 13.93% 的用户
    如果不用defaultdict, 可以优化到180ms
    """

    def __init__(self, arr, k):
        self.arr = arr
        self.k = k

    def check(self) -> bool:
        """
        返回arr是否能构成数组对
        """
        # 每个取余对应的数量
        # 比如 arr = [2, 5], k = 3
        # 那么 current_remain = {2: 2} 代表有2个数取余等于2
        current_remain = defaultdict(int)
        for i in self.arr:
            remain = i % self.k
            target = (self.k - remain) % (self.k)
            if current_remain[target] == 0:
                current_remain[remain] += 1
            else:
                current_remain[target] -= 1
        for i in current_remain.values():
            if i > 0:
                return False
        return True


class Solution2:
    """
    solution1里对current_remain进行了太多次的寻找和if判断, 我们这次先只遍历. 遍历时, 只增加current_remain. 少了if判断, 最后再对current_remain进行解析
    """

    def __init__(self, arr, k):
        # self.arr = arr
        self.values = defaultdict(int)
        for i in arr:
            self.values[i] += 1
        self.k = k

    def check(self) -> bool:
        """
        第一步, 先遍历arr, 得到所有余数的数量
        第二步, 根据余数排序, 从前往后匹配

        存在取余为0
        all_keys 0, 1, 2, 3, 4
        all_remain 4, x, y, y, x

        不存在取余为0
        all_keys  1, 2, 3, 4
        all_remain  x, y, y, x

        all_keys   2, 3, 4
        all_remain   y, y, x

        """
        current_remain = defaultdict(int)
        # 优化, 把所有的数字先汇总,然后一次性取余
        for value, cnt in self.values.items():
            current_remain[value % self.k] = cnt
        # for i in self.arr:
        #     current_remain[i % self.k] += 1
        all_remain = sorted(current_remain.values())
        # all_keys = sorted(current_remain.keys())
        all_remain_length = len(all_remain)
        if 0 in current_remain:
        # if all_keys[0] == 0:  # 存在取余为0
            if len(all_remain) % 2 != 1:
                return False
            for index in range(1, (all_remain_length + 1) // 2):
                if all_remain[index] != all_remain[all_remain_length - index]:
                    return False
            return True
        # 不存在取余为0
        if all_remain_length % 2 != 0:
            return False
        for index in range(0, all_remain // 2):
            if all_remain[index] != all_remain[all_remain_length - index - 1]:
                return False
        return True


class Solution3:
    """
    Solution2里面, 已经得到了所有的取余后的数字,
    那我们直接对这个dict进行循环就好了
    """

    def __init__(self, arr, k):
        # self.arr = arr
        self.values = defaultdict(int)
        for i in arr:
            self.values[i] += 1
        self.k = k

    def check(self) -> bool:
        """
        第一步, 先遍历arr, 得到所有余数的数量
        第二步, 根据余数排序, 从前往后匹配

        存在取余为0
        all_keys 0, 1, 2, 3, 4
        all_remain 4, x, y, y, x

        不存在取余为0
        all_keys  1, 2, 3, 4
        all_remain  x, y, y, x

        all_keys   2, 3, 4
        all_remain   y, y, x

        """
        current_remain = {}
        # 优化, 把所有的数字先汇总,然后一次性取余
        for value, cnt in self.values.items():
            if value % self.k not in current_remain:
                current_remain[value % self.k] = 0
            current_remain[value % self.k] += cnt
        # print(current_remain)
        if 0 in current_remain:
            if current_remain[0] % 2 != 0:
                return False
            del current_remain[0]
        # 处理中间值
        if self.k % 2 == 0:
            half = self.k // 2
            if half in current_remain:
                if current_remain[half] % 2 == 0:
                    del current_remain[half]
                else:
                    return False
        while current_remain:
            remain, cnt = current_remain.popitem()
            target = self.k - remain
            if target not in current_remain:
                return False
            if current_remain[target] == cnt:
                del current_remain[target]
                continue
            return False
        return True


class Solution4:
    """
    Solution3里面, 每次pop可能会导致dict内存重新
    申请, 所以我们这里只计算
    """

    def __init__(self, arr, k):
        # self.arr = arr
        self.values = defaultdict(int)
        for i in arr:
            self.values[i] += 1
        self.k = k

    def check(self) -> bool:
        """
        第一步, 先遍历arr, 得到所有余数的数量
        第二步, 根据余数排序, 从前往后匹配

        存在取余为0
        all_keys 0, 1, 2, 3, 4
        all_remain 4, x, y, y, x

        不存在取余为0
        all_keys  1, 2, 3, 4
        all_remain  x, y, y, x

        all_keys   2, 3, 4
        all_remain   y, y, x

        """
        current_remain = {}
        # 优化, 把所有的数字先汇总,然后一次性取余
        for value, cnt in self.values.items():
            if value % self.k not in current_remain:
                current_remain[value % self.k] = 0
            current_remain[value % self.k] += cnt
        # print(current_remain)
        if 0 in current_remain:
            if current_remain[0] % 2 != 0:
                return False
            del current_remain[0]
        # 处理中间值
        if self.k % 2 == 0:
            half = self.k // 2
            if half in current_remain:
                if current_remain[half] % 2 == 0:
                    del current_remain[half]
                else:
                    return False
        # 每个数字都会判断2次
        for remain, cnt in current_remain.items():
            target = self.k - remain
            if target not in current_remain:
                return False
            if current_remain[target] != cnt:
                return False
        return True


class Solution5:
    """
    Solution4里面, 所有的数据都会判断2次,
    实际上对我们来说 k=5时, 1和4是对称的.
    """

    def __init__(self, arr, k):
        # self.arr = arr
        self.values = defaultdict(int)
        for i in arr:
            self.values[i] += 1
        self.k = k

    def check(self) -> bool:
        """
        第一步, 先遍历arr, 得到所有余数的数量
        第二步, 根据余数排序, 从前往后匹配

        存在取余为0
        all_keys 0, 1, 2, 3, 4
        all_remain 4, x, y, y, x

        不存在取余为0
        all_keys  1, 2, 3, 4
        all_remain  x, y, y, x

        all_keys   2, 3, 4
        all_remain   y, y, x

        """
        current_remain = defaultdict(int)
        # 优化, 把所有的数字先汇总,然后一次性取余
        for value, cnt in self.values.items():
            remain = value % self.k
            if remain == 0:
                current_remain[0] += cnt
            elif remain <= (self.k // 2):
                current_remain[remain] += cnt
            else:
                current_remain[self.k - remain] -= cnt
        # print(current_remain)
        if 0 in current_remain:
            if current_remain[0] % 2 != 0:
                return False
            del current_remain[0]
        # 处理中间值
        if self.k % 2 == 0:
            half = self.k // 2
            if half in current_remain:
                if current_remain[half] % 2 == 0:
                    del current_remain[half]
                else:
                    return False
        # 每个数字都会判断2次
        for _, value in current_remain.items():
            if value != 0:
                return False
        return True


class Solution:
    """题目的基础框架"""

    def canArrange(self, arr, k) -> bool:
        """题目的基础框架"""
        return Solution5(arr, k).check()
