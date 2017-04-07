#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-04-07 18:04:56


class Solution(object):

    def findWords(self, words):
        row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        results = []
        for word in words:
            can = True
            if word == '':
                results.append(word)
            else:
                first = word[0].lower()
                if first in row1:
                    row = row1
                if first in row2:
                    row = row2
                if first in row3:
                    row = row3
            for character in word:
                if character.lower() not in row:
                    can = False
                    break
            if can:
                results.append(word)
        return results


if __name__ == '__main__':
    a = Solution()
    a.findWords(['Hello', 'Alaska'])
