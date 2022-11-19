#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    执行用时： 40 ms , 在所有 Python3 提交中击败了 88.74% 的用户
    内存消耗： 15 MB , 在所有 Python3 提交中击败了 40.75% 的用户
    """
    def deleteDuplicates(self, head):
        """
        a - b - c
        如果 b.val == a.val,
        那么 a.next = c
        """
        a = head
        if a is None:
            return a
        b = head.next
        if b is None:
            return a
        if b.next is None:
            if b.val == a.val:
                a.next = None
                return a
            return a
        c = b.next
        while c is not None:
            if a.val == b.val:
                a.next = c
                b, c = c, c.next
                continue
            a, b, c = b, c, c.next
        # 最后再次判断一下a, b
        if a.val == b.val:
            a.next = None
        return head
