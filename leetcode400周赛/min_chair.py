#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


class Solution:
    def minimumChairs(self, s: str) -> int:
        max_client_cnt: int = 0
        current_client_cnt: int = 0
        for i in s:
            if i == "E":
                current_client_cnt += 1
            elif i == "L":
                current_client_cnt -= 1
            else:
                raise ValueError("传的值不正确", i)
            max_client_cnt = max(current_client_cnt, max_client_cnt)
        return max_client_cnt
