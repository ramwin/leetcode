#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-06-02 15:21:23



import unittest
from collections import defaultdict


class Word(object):
    def __init__(self, word):
        self.chars = set(word)
        self.length = len(word)


class Solution_slow(object):
    """速度肯定太慢了啊, 最最基础的写法"""

    def maxProduct(self, words):
        maximum = 0
        for wordi in map(Word, words):
            for wordj in map(Word, words):
                if not (wordi.chars & wordj.chars):
                    maximum = max(maximum, wordi.length * wordj.length)
        return maximum


class Solution(object):
    """把单词和字母做关联，出现的单词就删除掉， 看剩下的最长是多长"""

    def maxProduct(self, words):
        words = set(words)
        maximum = 0
        character_dict = defaultdict(set)  # 每个字母下面有哪些word
        for word in words:
            for character in set(word):
                character_dict[character].add(word)
        for word in words:
            # print("当前最大: %d" % maximum)
            # print("现在处理word: %s" % word)
            remains = words.copy()
            # print("当前remains: %s" % remains)
            for character in word:
                remains = remains - character_dict[character]
            word_len = len(word)
            for word in remains:
                new = len(word) * word_len
                if new > maximum:
                    maximum = new
        return maximum


class SolutionTest(unittest.TestCase):

    def test_solution(self):
        a = Solution()
        self.assertEqual(a.maxProduct(['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef']), 16)


if __name__ == '__main__':
    unittest.main()
