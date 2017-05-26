#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-26 15:35:13


class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
