#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-26 16:03:13


# https://leetcode.com/problems/reverse-linked-list/#/description
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create_from_list(self, nums):
        head = nums[0]
        for i in len(nums):



class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        if head is None:
            return None
        next_node = head.next
        while next_node:
            origin_previous = previous
            previous = head
            head = head.next
            next_node = head.next
            previous.next = origin_previous
        head.next = previous
        return head
