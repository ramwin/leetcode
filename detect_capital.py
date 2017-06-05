#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-06-05 15:03:26


# https://leetcode.com/problems/detect-capital/#/description


class Solution(object):

    def detectCapitalUse(self, word):
        a = word[0:2]
        if len(a) < 2:
            return True
        # lowercase
        if a[1] > 'Z':
            for character in word[2:]:
                if character < 'a':
                    return False
        # Uppserclass
        if a[1] < 'a':
            if a[0] > 'Z':
                return False
            for character in word[2:]:
                if character > 'Z':
                    return False
        return True
