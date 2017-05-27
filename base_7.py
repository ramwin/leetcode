#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-27 14:04:58


# https://leetcode.com/problems/base-7/#/description

class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return '0'
        if num > 0:
            return ''.join(self.convert(num))
        else:
            return '-' + ''.join(self.convert(-num))

    def convert(self, num):
        if num == 0:
            return []
        s = num%7
        remain = (num-s)//7
        print('remain: %s' % remain)
        return self.convert(remain) + [str(s)]


a = Solution()
assert a.convertToBase7(7) == '10'
assert a.convertToBase7(100) == '202'
assert a.convertToBase7(-7) == '-10'
