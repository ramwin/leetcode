#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-12 17:09:31

# https://leetcode.com/problems/linked-list-random-node/#/description


import random
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head= ListNode(2)
head.next = ListNode(3)
head.next.next = ListNode(4)
class Solution(object):
    def __init__(self, head):
        self.head = head
        length = 1
        tmp = self.head.next
        while tmp is not None:
            length += 1
            tmp = tmp.next
        self.length = length
    
    def getRandom(self):
        index = 0
        result = self.head
        tmp = self.head.next
        while tmp:
            if random.randrange(0, index) == 0:
                result = tmp
            tmp = tmp.next
        return result
    def getRandom(self):
        index = random.randrange(0, self.length)
        tmp = self.head
        while index > 0:
            tmp = tmp.next
            index -= 1
        return tmp

a = Solution(head=head)
print(a.getRandom())
