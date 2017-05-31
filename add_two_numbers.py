#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-31 15:51:37


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):

        add = False
        if l1 is None and l2 is None:  # 不能都为空了
            return None
        if l1 is None:
            s = 0 + l2.val
        elif l2 is None:
            s = l1.val + 0
        else:
            s = l1.val + l2.val
        if s >= 10:
            add = True
            # l3 = ListNode(s-10)
            # if l1.next is None and l2.next is None:
            #     l3.next = ListNode(1)
            # else:
            #     if l1.next is None:
            #         l2.next.val += 1
            #     else:
            #         l1.next.val += 1
            #     l3.next = self.addTwoNumbers(l1.next, l2.next)

        else:
            # l3 = ListNode(s)
            # if l1 is None:
            #     l3.next = self.addTwoNumbers(None, l2.next)
            # if l2 is None:
            #     l3.next = self.addTwoNumbers(l1.next, None)
        return l3


a = ListNode(1)
b = ListNode(9)
b.next = ListNode(9)
c = Solution()
d = c.addTwoNumbers(a, b)
while d:
    print(d.val)
    d = d.next
