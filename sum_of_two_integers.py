#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-06-30 10:48:00

class Solution(object):
    def getSum(self, a, b):
        abin = bin(a)[2:]   # 101
        bbin = bin(b)[2:]   # 10
        self.max_len = max(len(abin), len(bbin))
        self.abin = abin.zfill(self.max_len)
        self.bbin = bbin.zfill(self.max_len)
        return self.sum_bin()

    def sum_bin(self):
        bin_str = ''
        add = 0
        for i in range(self.max_len-1, -1, -1):
            add = int(self.abin[i]) and int(self.bbin[i])
        if add:
            bin_str = '1' + bin_str
        return 

a = Solution()
print(a.getSum(1,2))
