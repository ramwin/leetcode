#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-27 17:43:39



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "TreeNode <val: %d>" % self.val

class Solution(object):

    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        all_results = []
        leve = 0
        next_list = [root]
        direction = True
        while True:
            results, next_list, direction = self.get_list(next_list, direction)
            all_results.append(results)
            if not next_list:
                break
        return all_results


    def get_list(self, previous_list, direction):
        """
            :type previous_list: List[Node],
                  direction: True or False,
            :rtype (result, next_list, direction)
                   result: List[int]
                   next_list: List[Node],
                   direction: False or True,
        """
        results = []
        next_list = []
        if direction is True:
            for node in previous_list:
                results.append(node.val)
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)
        else:
            length = len(previous_list)
            for index in range(len(previous_list)):
                node = previous_list[length-index-1]
                results.append(node.val)
                node = previous_list[index]
                if node.left:
                    next_list.append(node.left)
                if node.right:
                    next_list.append(node.right)
        return results, next_list, not direction


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.right.right = TreeNode(5)

b = Solution()
print(b.zigzagLevelOrder(a))
