#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-26 14:49:11

class Solution(object):
    def compareVersion(self, version1, version2):
        list1 = self.cutzero(version1)
        print('list1')
        print(list1)
        list2 = self.cutzero(version2)
        print('list2')
        print(list2)
        if list1 > list2:
            return 1
        if list1 == list2:
            return 0
        return -1

    @staticmethod
    def cutzero(text):
        import re
        text = text[:re.search(r'(\.0*)*$',text).start()]
        text = re.split(r'\.0*', (text.lstrip('0')))
        print(text)
        return map(
            lambda x: int(x) if x else 0,
            text
            )

s = Solution()
print(s.compareVersion('1.0','1'))
