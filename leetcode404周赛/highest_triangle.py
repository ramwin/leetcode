#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


class Solution:

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        max1 = self.get_max(red, blue)
        max2 = self.get_max(blue, red)
        return max(max1, max2)

    def get_max(self, first_color_number: int, second_color_number: int) -> int:
        level = 0
        cur_color_num = first_color_number
        next_color_num = second_color_number

        while True:
            level += 1
            if cur_color_num >= level:
                cur_color_num, next_color_num = next_color_num, (cur_color_num - level)
            else:
                break
        return level - 1
