#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-04-07 17:50:07


class Solution(object):

    def hammingDistance(self, x, y):
        bin_x = '%033d' % int(bin(x)[2:])
        bin_y = '%033d' % int(bin(y)[2:])
        cnt = 0
        for i in range(33):
            if bin_x[i] != bin_y[i]:
                cnt += 1
        return cnt
        


if __name__ == '__main__':
    a = Solution()
    print(a.hammingDistance(1, 4))
