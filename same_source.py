#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
https://leetcode.cn/problems/check-if-an-original-string-exists-given-two-encoded-strings/
"""

import re


BASE_STRING = {'c', 'o', 'q', 'r', 'u', 'z', 'i', 'x', 'y', 'k', 'v', 'f', 'e', 'p', 'h', 'm', 'w', 'j', 'a', 'd', 'b', 's', 't', 'l', 'g', 'n'}


# 方案一
class MyString:
    """
    字符串对象, 需要实现切割, 比较, 消灭同类项的功能
    """
    def __init__(self, s, first_number_width=None):
        """
        first_number_width: 是否限定一个数字的长度
        如果限定了, 那么第一个数字只能-1, 不能当作字符串切割
        """
        self.origin_string = s
        self.split_by_letter = self.string_2_list(self.origin_string)
        self.first_number_width = True  # 第一个数字能否split, 如果数字-1过了, 就不能再split了

    @staticmethod
    def string_2_list(string):
        """
        把一个字符串根据字符切割
        '123l45' => ['123', 'l', '45']
        start 0
        match: 3, 4
        """
        # TODO 如果限制了第一个数字的宽度, 需要考虑
        result = []
        start = 0
        end = 0
        for match in re.finditer("[a-z]", string):
            if match.start() != start:
                result.append(
                    string[start: match.start()]
                )
            result.append(match.group())
            start = end = match.end()
        if end != len(string):
            result.append(string[end:])
        return result

    def is_same_source(self, other) -> bool:
        if len(self.split_by_letter) == 0 and len(other.split_by_letter) == 0:
            return True
        elif len(self.split_by_letter) == 0 or len(other.split_by_letter) == 0:
            return False
        # 字符串都是字母开头
        first_item = self.split_by_letter[0]
        first_other_item = other.split_by_letter[0]
        if first_item == first_other_item and first_item in BASE_STRING:
            return MyString(self.origin_string[1:]).is_same_source(MyString(other.origin_string[1:]))

        # 字符串都是数字开头
        # TODO 这里要考虑利用start, end 来做缓存
        if first_option.start_width_number() and other.start_width_number():
            for first_option in self.split_first_number():
                for second_option in other.split_first_number():
                    if first_option.is_same_source(second_option):
                        return True
        # other是字符开头
        if self.start_width_number() and other.start_width_letter():
            return other.is_same_source(self)
        if self.start_width_letter() and other.start_width_number():
            for second_option in other.split_first_number():
                second_option = second_option.minuse_one()
                if second_option.is_same_source(MyString(self.origin_string[1:])):
                    return True
        raise Exception("逻辑有问题")

    def minuse_one(self):
        """把第一个元素的数字减一来匹配"""
        raise NotImplementedError

    def split_first_number(self):
        """
        把 [43, ...] 变成2个元素
            [4, 3, ...]
            [43, ...]
        """
        assert re.match("^[1-9]+$", self.split_by_letter[0])
        if len(self.split_by_letter[0]) == 1:
            return [MyString(self.origin_string, first_number_width=1)]
        return [
            MyString(self.origin_string, first_number_width=width)
            for width in range(1,
                               len(self.split_by_letter[0]) + 1):
        ]

class Solution:
    """
    s1 = l123e
    s2 = 44
    任意一个字符串, 都可以通过字母来切割成 [a, b, c]
    s1 = [l, 123, e]
    s2 = [44]
        对应分支1: [4, 4]
        对应分支2: [44, ]
    如果s1和s2前面都是字母, 那必定要一致才能匹配
    如果s1, s2前面都是数字, 那么只要相减, 就可以认为匹配.
        比如 s1 = [2, 3, 2]
             s2 = [1, 3, 2]
        那么只要判断 s1 [1, 3, 2] 是否 = s2 [3, 2] 即可
    如果s1前面是字母, s2前面是数字
        s1 = [l, 123, e] => [123, e]
            分支1 s2 = [4, 4] => [3, 4]
            分支2 s2 = [44, ] => [43, ]
                => 此时 [43, ] 后续转化时, 不能变成 [4, 3]
    """
