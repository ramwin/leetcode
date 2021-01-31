#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-04-06 10:16:30


def get_cnt(a):
    result = {}
    cnt = 0
    for i in a:
        if i in result:
            result.pop(i)
            cnt += 1
        else:
            result[i] = True
    return cnt



assert get_cnt([1,2,1,2,1,3,2, 2,2])== 3
assert get_cnt([10,20,20,10,10,30,50,10,20]) == 3
