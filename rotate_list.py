#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-06-07 10:01:53


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        if k == 0:
            return head
        if head.next == None:
            return head
        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1
        node.next = head
        if k >= length:
            return head
        for i in range(length - k):
            node = node.next
        head = node.next
        node.next = None
        return head


a = ListNode(1)
s = Solution()
b = s.rotateRight(a, 1)
print(b.val)
print(b.next)
