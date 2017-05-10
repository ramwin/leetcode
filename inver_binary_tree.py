#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-10 11:28:41


# Definition for a binary tree node.

# https://leetcode.com/problems/invert-binary-tree/#/description

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invertNode(root)
        return root

    def invertNode(self, node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.invertNode(node.left)
        self.invertNode(node.right)


import unittest

class TestSolution(uniitest.TestCase):

    def test_solution(self):
        treenode = TreeNode(4)
        treenode.left = TreeNode(2)
        treenode.left.left = TreeNode(1)
        treenode.left.right = TreeNode(3)
        treenode.right = TreeNode(7)
        treenode.right.left = TreeNode(6)
        treenode.right.right = TreeNode(9)
        s = Solution()
        # too many test code, let's just run it in leetcode


if __name__ == '__main__':
    unittest.main()
