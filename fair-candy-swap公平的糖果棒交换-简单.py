#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 击败64.45% 11.25%
# 改成set击败 49.36% 14.92%
# 改成dict
class Solution1:
    def fairCandySwap(self, A, B):
        diff = (sum(A) - sum(B)) // 2
        if diff == 0:
            return [0,0]
        # b = frozenset(B)
        b = {
                i: True for i in B
        }
        for i in A:
            if (i-diff) in b:
                return [i, i-diff]


# 64.45% 37.69%
class Solution:
    def fairCandySwap(self, A, B):
        A.sort()
        # print(f"A: {A}")
        B.sort()
        # print(f"B: {B}")
        diff = (sum(A) - sum(B)) // 2  # A比B多的
        # print(f"diff: {diff}")
        i = j = 0
        while True:
            # print(f"i: {i}, j: {j}")
            if A[i] - B[j] == diff:
                return [A[i], B[j]]
            if A[i] - diff >= B[j]:
                j+=1
                continue
            i+=1
            continue


# 
class Solution:
    def fairCandySwap(self, A, B):
        # print(f"A: {A}")
        # print(f"B: {B}")
        diff = (sum(A) - sum(B)) // 2  # A比B多的
        # print(f"diff: {diff}")
        i = j = 0
        while True:
            # print(f"i: {i}, j: {j}")
            if A[i] - B[j] == diff:
                return [A[i], B[j]]
            if A[i] - diff >= B[j]:
                j+=1
                continue
            i+=1
            continue


solution = Solution1()
assert solution.fairCandySwap([1,1], [2,2]) == [1,2]
assert solution.fairCandySwap([1,2,5], [2,4]) == [5,4]
