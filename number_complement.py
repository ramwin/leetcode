#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-04-07 18:00:26


class Solution(object):
    def findComplement(self, num):
        result = ''
        for i in bin(num)[2:]:
            result += '0' if i == '1' else '1'
        return int(result, 2)
        


if __name__ == '__main__':
    a = Solution()
    print(a.findComplement(1))
