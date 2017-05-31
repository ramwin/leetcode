#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-31 11:31:29


# https://leetcode.com/problems/text-justification/#/description


import unittest


class Solution(object):
    def get_text(self):
        if self.end == self.length:
            result = ""
            for word in self.words[self.start:self.end]:
                result += word + " "
            missing = self.maxWidth - len(result)
            if missing > 0:
                return result + " " * missing
            if missing < 0:
                return result.strip()
            else:
                return result
                
        character_total = 0
        for word in self.words[self.start:self.end]:
            character_total += len(word)
        space_cnt = self.maxWidth - character_total
        blank_count = self.end - self.start - 1
        if blank_count == 0:
            return self.words[self.start] + " " * space_cnt
        else:
            result = ""
            base_space_count = space_cnt//blank_count
            extra_space_count = space_cnt//blank_count + 1
            extra_space_times = space_cnt % blank_count
            for i in range(blank_count):
                if i < extra_space_times:
                    result += self.words[self.start+i] + " " * extra_space_count
                else:
                    result += self.words[self.start+i] + " " * base_space_count
            result += self.words[self.start + blank_count]
            return result

    def fullJustify(self, words, maxWidth):
        self.words = words
        self.maxWidth = maxWidth
        self.start = 0  # 起始的word
        self.end = 0  # 终止的word
        result = []
        current_length = 0
        length = len(words)
        self.length = length

        while self.end < length:
            current_length += len(self.words[self.end]) + 1
            if current_length <= maxWidth + 1:
                self.end += 1
            else:
                result.append(self.get_text())
                self.start = self.end
                current_length = 0
        if self.start != self.end:
            result.append(self.get_text())
        return result


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        a = Solution()
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        results = [
           "This    is    an",
           "example  of text",
           "justification.  "
        ]
        self.assertEqual(a.fullJustify(words, 16), results)
        words = ["What","must","be","shall","be."]
        results = ["What must be","shall be.   "]
        self.assertEqual(a.fullJustify(words, 12), results)


if __name__ == '__main__':
    unittest.main()
