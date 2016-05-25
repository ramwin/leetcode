#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-25 15:22:49


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):

    def getIntersectionNode(self, headA, headB):
        '''
        :type head1, head1: ListNode
        :rtype: ListNode
        '''
        store = {}
        if not headA or not headB:
            return None
        store[headA.val] = True
        b = headA.next
        while True:
            print('b')
            if not b:
                break
            store[b.val] = True
            b = b.next
        print(store)
        if store.get(headB.val):
            return headB
        c = headB.next
        while True:
            print('c')
            if not c:
                break
            if store.get(c.val):
                return c
            c = c.next
        return None

A = [1,3,5,7,9,11,13,15,17,19,21]
B = [19,21]
As = []
Bs = []
for i in A:
    As.append(ListNode(i))
for i in B:
    Bs.append(ListNode(i))
for i in range(len(A)-1):
    As[i].next = As[i+1]
for i in range(len(B)-1):
    Bs[i].next = Bs[i+1]

print(Bs[0].val)
a = Solution()
print(a.getIntersectionNode(As[0],Bs[0]).val)
