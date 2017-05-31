#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-31 15:51:37


# https://leetcode.com/problems/add-two-numbers/#/description


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
            l1 = ListNode(0)
        elif l2 is None:
            l2 = ListNode(0)
        s = l1.val + l2.val
        if s >= 10:
            add = 1
            s = s - 10
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
            add = 0
            # l3 = ListNode(s)
            # if l1 is None:
            #     l3.next = self.addTwoNumbers(None, l2.next)
            # if l2 is None:
            #     l3.next = self.addTwoNumbers(l1.next, None)
        l3 = ListNode(s)
        if add:
            if l1.next is None:
                l1.next = ListNode(1)
            else:
                l1.next.val += 1
        l3.next = self.addTwoNumbers(l1.next, l2.next)
        return l3


a = ListNode(1)
b = ListNode(9)
b.next = ListNode(9)
c = Solution()
d = c.addTwoNumbers(a, b)
while d:
    print(d.val)
    d = d.next
