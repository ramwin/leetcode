#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-04-04 08:34:39


class Solution:
    def addToArrayForm(self, A, K: int):
        return list(map(
            int,
            str(
                int("".join(map(str, A))) + K
            )
        ))



solution = Solution()
print(solution.addToArrayForm([2,7,4], 181))
