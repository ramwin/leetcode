#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2021-01-31 21:33:03

from collections import defaultdict


class Solution:

    def numSimilarGroups(self, strs: List[str]) -> int:
        groups = []
        base_string = strs[0]
        for string in strs:
            diff = get_diff(base_string, string)
            for group in groups:
                # bug: 如果一个string同时处于2个group需要merge
                if diff in group:
                    group.add_diff(diff)
                else:
                    group = Group()
                    group.add_diff(diff)
                    groups.append(group)
        return len(groups)


class Group(object):

    def __init__(self):
        self.

    def __contains__(self, diff):

def get_diff(source, target):
    return {
        index: ord(strb) - ord(stra)
        for index, (stra, strb) in enumerate(zip(source, target))
        if stra != strb
    }


assert Solution().numSimilarGroups(["tars","rats","arts","star"]) == 2
assert Solution().numSimilarGroups(["omv","ovm"]) == 1
