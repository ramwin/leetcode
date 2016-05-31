#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-26 17:39:02

class Solution(object):
    def singleNumber(self, nums):
        """
        basic solution
        :type nums: List[int]
        :rtype: int
        """
        a = set()
        b = set()
        for num in nums:
            if num in b:
                continue
            elif num in a:
                a.discard(num)
                b.add(num)
            else:
                a.add(num)
            print('a is {0}'.format(a))
            print('b is {0}'.format(b))
        return a.pop()
    def singleNumber2(self, nums):
        """
            save memory
            查看了别人的代码，使用每个数字的每个比特求和，除以3的余数就是结果

        """
        pass


a = Solution()
print(a.singleNumber([2,2,3,2]))
