#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
给你一个房屋数组houses 和一个整数 k ，其中 houses[i] 是第 i 栋房子在一条街上的位置，现需要在这条街上安排 k 个邮筒。

请你返回每栋房子与离它最近的邮筒之间的距离的 最小 总和。

答案保证在 32 位有符号整数范围以内。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/allocate-mailboxes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from decimal import Decimal
from functools import lru_cache
import logging
from typing import List


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


# 方案一

class HouseList:
    """
    封装和房子有关的所有信息
    22 / 69 个通过测试用例 超出时间限制
    最后执行的输入：
    [48,23,44,42,2,7,25,18,32,20,36,31,30,26,10,33,22,9,1,35]
    15
    """

    def __init__(self, houses):
        self.houses = sorted(houses)
        self.house_index = {  # 通过位置,快速知道这是第几个house
            house_position: index
            for index, house_position in enumerate(self.houses)
        }
        self.length = len(self.houses)

    def iter_start_end(self, start_index, end_index):
        """
        把房子列表[start_index:end_index]拆分成左右2个列表
        _index 指房间的序号ID(0, 1, 2, ...)
        _position 指房间位置(3, 6, 9)
        left_index 指左边的房子列表里, 最后一个房子的序号
        right_index 指右边的房子列表里, 第一个房子的序号
        return [
            [left_index, right_index],
        ]
        """
        assert (end_index - start_index) >= 2
        for i in range(start_index, end_index - 1):
            yield [i, i+1]

    def get_total_distance(self, start_index, end_index):
        """
        返回 houses[start:end] 在 mail_box_position 放置一个邮筒时, 距离的求和
            当邮筒数量为1是, 放在中间位置
            a, b, c, d 邮筒 A B C D 只要在d与A之间即可(邮筒左右移动时, 左右4个房子同时+1, 或者-1
            a, b, c 邮筒(D) A B C 如果是奇数, 邮筒就在D的位置上
                start_index = 0, end_index = 7  返回 houses[3]
        """
        result = 0
        mail_box_position = self.houses[(end_index - start_index) // 2 + start_index]
        for house_position in self.houses[start_index: end_index]:
            result += abs(house_position - mail_box_position)
        return result

    def __str__(self):
        return str(self.houses)


class MySolution:
    """
    找某个地址x, 邮箱分为左边 n 个, 右边 k-n个.
    那么距离最小总和 = 左边的距离求和 + 右边的距离求和
    """

    def __init__(self, houses, k):
        self.house_list = HouseList(houses)
        self.k = k

    @lru_cache(maxsize=None)
    def get_result(self, start_index, end_index, cnt) -> int:
        """
        返回在houses[start: end]之间,放置cnt个邮筒, 所生成的距离最小的综合
        标准的左闭右开区间(不包括end)
        """
        if cnt >= (end_index - start_index):
            min_result = 0
        elif cnt == 1:
            min_result = self.house_list.get_total_distance(
                start_index, end_index)
        else:
            min_result = Decimal("inf")
            for left_index, right_index in self.house_list.iter_start_end(start_index, end_index):
                # 左边index是0的话, 最多只能给1个邮箱
                for left_cnt in range(cnt - 1, 0, -1):
                    # 左边 houses[0: x] 放置left_cnt个邮筒
                    left_result = self.get_result(0, left_index + 1, left_cnt)
                    if left_result >= min_result:
                        break
                    # 右边 houses[x: ] 放置 self.k - left_cnt个邮筒
                    right_result = self.get_result(
                        right_index, end_index, cnt - left_cnt)
                    result = left_result + right_result
                    min_result = min(min_result, result)
        logger.info((
            "%s:%s放置%s个邮箱需要: "
            "%s 距离"),
            start_index, end_index, cnt, min_result,
        )
        return min_result


class Solution:
    """兼容leetcode"""

    def minDistance(self, houses: List[int], k: int) -> int:
        """返回最小距离"""
        return MySolution(houses, k).get_result(0, len(houses), k)
