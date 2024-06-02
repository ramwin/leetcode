#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import heapq


class Solution:
    """
    ab*cd*

    转化成列表 ['a', 'b', '*', 'c', 'd', '*'], 如果删除就变成 ['a', 'b', '', 'c', 'd', '*']

    """
    def clearStars(self, s: str) -> str:
        sorted_list: List[Tuple[str, index]] = []
        for index, char in enumerate(s):
            if char == '*':
                heapq.heappop(sorted_list)
            else:
                heapq.heappush(sorted_list, (char, -index))
        sorted_list.sort(key=lambda x: -x[1])
        return "".join((
            char[0]
            for char in sorted_list
            if char[0] != '*'
        ))
