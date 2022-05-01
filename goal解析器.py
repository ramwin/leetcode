#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import enum


class Status(enum.Enum):
    NORMAL = 1
    FIRST_BRACKET = 2
    IN_BRACKET = 3


class Solution:

    def interpret(self, command: str) -> str:
        result = ""
        status = Status.NORMAL
        for i in command:
            if i == "G":
                result += "G"
            elif i == "(":
                status = Status.FIRST_BRACKET
            elif i == ")":
                if status == Status.FIRST_BRACKET:
                    result += "o"
                elif (status == Status.IN_BRACKET):
                    result += 'al'
            else:
                status = Status.IN_BRACKET
        return result


print(Solution().interpret("G()(al)"))
