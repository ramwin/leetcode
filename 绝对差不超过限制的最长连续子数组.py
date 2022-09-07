#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

"""
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

如果不存在满足条件的子数组，则返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/
longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from bisect import bisect_left, insort, bisect_right
from collections import defaultdict
import logging


LOGGER = logging.getLogger("absolute")


def rm(num_list, item):
    """从l中移除item"""
    num_list.pop(bisect_left(num_list, item))


class Number:
    """我是一个数字"""

    def __init__(self, index, value, limit):
        self.index = index
        self.value = value
        self.minimum = value - limit
        self.maximum = value + limit
        self.end = None  # 我和后面哪个数字的绝对差超过了limit

    def __hash__(self):
        return self.index

    def __str__(self):
        return f"({self.value}, index={self.index})"

    def __repr__(self):
        return str(self)


class Solution:
    """
    思路一: 动态规划
    nums = [8,2,4,7], limit = 4

    已经计算好了 8 2 4的情况下, 考虑是不是要把7加进来
    1. 只取8,2,4
    2. 把7加进来. 这样就要知道 [8, 2, 4]里面能有多少处于 [7-4 ~ 7+4]

    重点: 实现算法,从后往前找到数组里面超出指定范围的第一个元素(难)

    思路二:
        对于每个元素来说, 都存在我需要限定的范围
        [8, 2, 4, 7]
        对于8, 如果后面的数字不在 8-4 ~ 8+4 之间, 那认为8走到的尽头
        0. 第0步:
            8: [4, 12]
        1. 第1步:
            2走进来, 不属于4~12之间, 所以8剔除
            2: [-2, 6]
        2. 第2步:
            4走进来.
            2: [-2, 6]
            4: [0, 8]
        3. 第3步:
            7走进来, 不属于 -2~6之间, 所以2剔除
            4: [0, 8]
            7: [3, 11]
        # TODO 如果来了一个数, 导致前面有个很大得绝对差数字无法计算, 那么这个数之前的所有元素, 都只能到这个数停止
    步数: n
    每一个n, 我们要找所有n-1的元素, 找到里面最大值小于 n的值 - limit
        或者 最小值大于 n的值+limit的 log(n-1)
        n * log(n-1)
    """

    def __init__(self, nums, limit):
        """
        [8, 2, 4, 7] limit = 4的时候, 当前已经处理好了 8, 2, 4
        minimum = [-2, 0]
        minimum_dict = {-2: {Number(2)}, 0: {Number(4)}}
        maximum = [6, 8]
        # XXX 可以反过来, 方便切割后面的部分
        maximum_dict = {6: {Number(2)}, 8: {Number(4)}}
        当7走进来的时候, maximum < 7, minimum > 7 可以直接二分法, 找到minimum =
            举例 数字2, 对于limit4来说, 他的范围只能是 [-2, 6] 7> maximum(2)
                 数据12, 他的minimum = (12-4)=8 > 7
        """
        self.nums = [
            Number(index, value, limit)
            for index, value in enumerate(nums)
        ]
        # XXX 优化, minimum和maximum可以用堆
        self.minimum = []  # 当前寻找中的数字所能接受的最小值(唯一的,排序好的列表)
        self.minimum_dict = defaultdict(set)
        self.maximum = []  # 挡墙寻找中的数字所能接受的最大值
        self.maximum_dict = defaultdict(set)
        # XXX 如果用列表, 是不是可以更快得找出来
        self.handling_nums = set()  # 排序好的数字

    def inspect_number(self, number):
        """
        当存在数字(limit=4)
            6: [2, 10]
            10: [6, 14]
            1: [-3, 5]

        时, 如果来了一个5, 会导致6失败, 10失败 但是1可以继续

        处理一个number, 移除自身的不符合的
            minimum,
            minimum_dict,
            maximum,
            maximum_dict
            handling_nums,
        属性
        """
        LOGGER.debug("处理%s", number)
        LOGGER.debug("最小值处理前:")
        LOGGER.debug("minimum: %s", self.minimum)
        LOGGER.debug("minimum_dict: %s", self.minimum_dict)
        minimum_index = self.get_minimu_index(number.value)
        LOGGER.debug("minimum_index: %s", minimum_index)
        for minimum_num in self.minimum[minimum_index:]:
            for num in self.minimum_dict[minimum_num]:
                if num.end is None:
                    num.end = number.index  # 这些num因为误差范围超过了limit而被移除
                self.remove_max_num(num)
                self.remove_index_less_than(num, number)
            del self.minimum_dict[minimum_num]
        LOGGER.debug("最小值处理后:")
        LOGGER.debug("minimum: %s", self.minimum)
        LOGGER.debug("minimum_dict: %s", self.minimum_dict)
        self.minimum = self.minimum[0: minimum_index]
        # 最大值不符合的数据移除
        maximum_index = self.get_maximum_index(number.value)
        LOGGER.debug("number的maximum: %s", number.maximum)
        LOGGER.debug("最大值: %s", self.maximum)
        LOGGER.debug("maximum_index: %s", maximum_index)
        LOGGER.debug("最大值不符合要求的数据有: %s", self.maximum[0:maximum_index])
        for maximum_num in self.maximum[0:maximum_index]:
            for num in self.maximum_dict[maximum_num]:
                if num.end is None:
                    num.end = number.index
                self.remove_min_num(num)
                self.remove_index_less_than(num, number)
            del self.maximum_dict[maximum_num]
        self.maximum = self.maximum[maximum_index:]
        LOGGER.debug("最大值处理后:")
        LOGGER.debug("minimum: %s", self.minimum)
        LOGGER.debug("minimum_dict: %s", self.minimum_dict)

    def get_result(self):
        """
         对应的实际     10,12
        对于 minimum = [6, 8]来说, 如果出现一个数字是7, 那么minimum > 7的
            即8(index=1)就不在符合要求
        """
        for number in self.nums:
            # 最小值不符合的数据移除
            self.inspect_number(number)
            self.insert_number(number)
        final_index = len(self.nums)
        for num_set in self.minimum_dict.values():
            for num in num_set:
                num.end = final_index
        for num_set in self.maximum_dict.values():
            for num in num_set:
                num.end = final_index
        return max((
            num.end - num.index
            for num in self.nums
        ))

    def get_maximum_index(self, number):
        """
        找到最大值不符合要求的对应的索引
        这个index,本身是符合要求的
        [0, 1, 2] = 2  => 2
        [0, 2] = 1 => 0
        [0, 2] = 0 => 0
        [6] = -2 => 0
        """
        index = bisect_left(self.maximum, number)
        return index

    def remove_index_less_than(self, num, end_num):
        """如果一个数字被移除了, 那么他之前所有得数字也要被移除"""
        for pre_num in self.handling_nums:
            if pre_num.index < num.index:
                if pre_num.end is None:
                    pre_num.end = end_num.index

    def remove_max_num(self, number):
        """
        把一个数字, 从max的可选项里面移除
        """
        LOGGER.debug("%s需要从max移除", number)
        if number.maximum in self.maximum_dict:
            if number in self.maximum_dict[number.maximum]:
                self.maximum_dict[number.maximum].remove(number)
                if not self.maximum_dict[number.maximum]:
                    rm(self.maximum, number.maximum)
                    del self.maximum_dict[number.maximum]

    def remove_min_num(self, number):
        """
        把一个数字, 从min可选项里面移除
        """
        LOGGER.debug("%s需要从min移除", number)
        if number.minimum in self.minimum_dict:
            if number in self.minimum_dict[number.minimum]:
                self.minimum_dict[number.minimum].remove(number)
                if not self.minimum_dict[number.minimum]:
                    rm(self.minimum, number.minimum)
                    del self.minimum_dict[number.minimum]

    def insert_number(self, number):
        """把number插入带寻找范围的列表和词典里"""
        # minimum的处理
        if number.minimum in self.minimum_dict:
            pass
        else:
            insort(self.minimum, number.minimum)
        self.minimum_dict[number.minimum].add(
            number
        )
        # maximum的处理
        if number.maximum in self.maximum_dict:
            pass
        else:
            insort(self.maximum, number.maximum)
        self.maximum_dict[number.maximum].add(
            number
        )
        self.handling_nums.add(number)

    def get_minimu_index(self, number):
        """
        找到当前最小值不符合的索引值
        """
        return bisect_right(self.minimum, number)
