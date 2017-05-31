#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-31 14:38:31


# https://leetcode.com/problems/palindrome-partitioning/#/description

import unittest


class Solution(object):

    def is_palindrome(self, s):
        """判断一个字符串是不是回文"""
        return "".join(reversed(s)) == s
        if "".join(reversed(s)) == s:
            print("字符串: <%s> 是回文" % s)
            return True
        else:
            print("字符串: <%s> 不是回文" % s)
            return False
            

    def partition(self, s):
        # try:
        # if True:
        # print("获取字符串<%s>的所有可能" % s)
        if len(s) == 0:
            return [[],]
        if len(s) == 1:
            return [[s], ]
        result = []
        for i in range(1, len(s)+1):
            if self.is_palindrome(s[0:i]):
                first_word = s[0:i]
                for sub_result in self.partition(s[i:]):
                    a = [first_word, ]
                    b = sub_result
                    # print("a: %s" % a)
                    # print("b: %s" % b)
                    result.append([first_word, ] + sub_result)
        # print("字符串<%s>的所有可能有: " % s)
        # print("    ", end="")
        # print(result)
        return result
        # except Exception as e:
        # else:
        #     print(e)
        #     import ipdb
        #     ipdb.set_trace()


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        cin = "aab"
        cout = [
            ["a", "a", "b"],
            ["aa", "b"],
        ]
        a = Solution()
        self.assertEqual(a.partition(cin), cout)
        cin = "bb"
        cout = [
            ["b", "b"],
            ["bb"],
        ]
        self.assertEqual(a.partition(cin), cout)
        cin = "efe"
        cout = [
            ["e", "f", "e"],
            ["efe"],
        ]
        self.assertEqual(a.partition(cin), cout)


if __name__ == '__main__':
    unittest.main()
