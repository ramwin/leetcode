#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
测试
"""


import unittest

from most_score_words import Solution1


class Test(unittest.TestCase):
    """基础测试"""

    def setUp(self):
        """创建solution"""
        words = ["dog", "cat", "dad", "good"]
        letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
        self.score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.solution = Solution1(words, letters, self.score)

    def test_create(self):
        """测试构建"""
        solution = self.solution
        self.assertEqual(
            solution.word_instances[2].score,
            11,
        )
        self.assertEqual(
            solution.word_instances[3].word,
            "good",
        )
        self.assertEqual(
            solution.word_instances[1].index,
            1,
        )

    def test_get_remain_letters(self):
        """测试从letters中移除word"""
        solution = self.solution
        word = 'abc'
        letters = ['d', 'e', 'f', 'a', 'a', 'b', 'c']
        self.assertEqual(
            solution.get_remain_letters(word, letters),
            ['d', 'e', 'f', 'a']
        )
        self.assertEqual(
            solution.get_remain_letters('z', letters),
            None,
        )

    def test_get_result(self):
        """测试get_max_score"""
        solution = Solution1(
            words=["dog"],
            letters=["a","a","c","d","d","d","g","o","o"],
            score=self.score
        )
        self.assertEqual(
            solution.get_max_score(
                solution.word_instances, solution.letters),
            10,
        )
        self.assertEqual(
            self.solution.get_max_score(
                self.solution.word_instances,
                self.solution.letters,
            ),
            23,
        )
