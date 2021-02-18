#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-02-02 10:59:34


import heapq
from collections import defaultdict


class Solution:

    def characterReplacement(s, k):
        self.start = 0
        self.end = 0
        self.same_max = 0
        result = 0
        current_same = 0
        self.letter_dict = defaultdict(int)  # 通过letter查数量
        self.number_letter = defaultdict(set)  # 通过数量查letter
        for letter in s:
            self.add_letter(letter)
            current_len = self.end - self.start
            if self.same_max >= current_len-k:
                current_same = max(
                    current_same,
                    current_len,
                )
            else:
                self.end += 1
                self.remove_letter(s[self.start])

    def add_letter(self, letter):
        self.end += 1
        before_cnt = self.letter_dict[letter]
        after_cnt = before_cnt + 1
        self.letter_dict[letter] = after_cnt
        self.same_max = max(
            self.letter_dict[letter],
            self.same_max
        )
        self.number_letter[after_cnt].add(letter)
        self.number_letter[before_cnt].

    def remove_letter(self, letter):
        self.start += 1
        self.letter_dict[letter] -= 1
