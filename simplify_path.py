#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-25 16:02:33

class Solution(object):
    def simplifyPath(self, path):
        import os
        return os.path.abspath(path)


a = Solution()
print(a.simplifyPath('/home/'))
