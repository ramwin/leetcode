#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-06-01 16:10:30


# https://leetcode.com/problems/word-ladder/#/description


import unittest
from collections import defaultdict

'''
    depth_dict = {
        0: [endWord],
        1: [word1, word2],
        2: [word3, word4, word5],
        ...
    }
'''
class Solution(object):

    def isadjacent(self, word1, word2):
        if "%s_%s" % (word1, word2) in self.not_adjacent or \
            "%s_%s" % (word2, word1) in self.not_adjacent:
            return False
        result = True
        for a, b in zip(word1, word2):
            if a != b:
                if result == False:  # the character diffs for the 2nd time.
                    self.not_adjacent["%s_%s" % (word1, word2)] = True
                    return False
                else:
                    result = False
        return True

    def ladderLength(self, beginWord, endWord, wordlist):
        self.not_adjacent = {}
        depth_dict = defaultdict(list)
        if endWord not in wordlist:
            return 0
        depth_dict[0] = [endWord, ]
        wordlist.remove(endWord)
        depth = 0
        while depth_dict[depth]:
            depth += 1
            for word1 in wordlist:
                for word2 in depth_dict[depth-1]:
                    if self.isadjacent(word2, beginWord):
                        if word2 == beginWord:
                            return depth
                        return depth + 1
                    if self.isadjacent(word1, word2):
                        try:
                            wordlist.remove(word1)
                        except:
                            pass
                        depth_dict[depth].append(word1)
        for word in depth_dict[depth]:
            if self.isadjacent(word, beginWord):
                if word == beginWord:
                    return depth + 1
                return depth + 2
        return 0


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        a = Solution()
        self.assertEqual(a.ladderLength('hit', 'cog', [
            'hot', 'dot', 'dog', 'lot', 'log','cog'
        ]), 5)
        self.assertEqual(a.ladderLength('hot', 'dog', [
            'hot', 'dog'
        ]), 0)
        self.assertEqual(a.ladderLength('hit', 'cog', [
            'hot', 'dot', 'dog', 'log', 'log'
        ]), 0)
        self.assertEqual(a.ladderLength('hot', 'dog', [
            'hot', 'dog', 'dot'
        ]), 3)

if __name__ == '__main__':
    unittest.main()
