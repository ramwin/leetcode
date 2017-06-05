#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-06-02 16:42:38


class Solution(object):

    def pathSum(self, root, sum, must_with_root=False, not_null=True):
        # must_with_root, whether the root should be included
        # not_null whether the root link can be none
        if with_root is False:
            left_cnt = self.pathSum(root.left, sum)
            right_cnt = self.pathSum(root.right, sum)
            middle_cnt = self.pathSum(root.left, sum-root.val, must_with_root=True) + self.pathSum(root.right, sum-root.val, must_with_root=True)
