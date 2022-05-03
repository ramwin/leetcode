#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


# 执行用时： 32 ms , 在所有 Python3 提交中击败了 92.68% 的用户
# 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 55.28% 的用户

# 用property优化内存后
# 执行用时： 48 ms , 在所有 Python3 提交中击败了 5.89% 的用户
# 内存消耗： 15 MB , 在所有 Python3 提交中击败了 98.17% 的用户

# 用key避免每次创建Log对象
# 执行用时： 48 ms , 在所有 Python3 提交中击败了 5.89% 的用户
# 内存消耗： 15 MB , 在所有 Python3 提交中击败了 97.36% 的用户


class Log:

    def __init__(self, string):
        self.string = string
        # 用property来减少内存
        # self.prefix, self.suffix = string.split(" ", 1)
        # self.is_number = self.suffix[0].isdigit()

    @property
    def is_number(self):
        return self.suffix[0].isdigit()

    @property
    def prefix(self):
        return self.string.split(" ", 1)[0]

    @property
    def suffix(self):
        return self.string.split(" ", 1)[1]

    def __lt__(self, log):
        if self.is_number:
            if log.is_number:
                return False
            else:
                return False
        else:
            if log.is_number:
                return True
            else:
                return (self.suffix, self.prefix) < (log.suffix, log.prefix)

    @classmethod
    def cmp(cls, string1, string2):
        return cls(string1) < cls(string2)


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        logs.sort(
            key=lambda x: Log(x)
        )
        return logs
