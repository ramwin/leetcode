#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-31 15:26:09


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/#/description


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root.val == p.val or root.val == q.val:
            return root
        else:
            if p.val < root.val < q.val or q.val < root.val < p.val:
                return root
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)
