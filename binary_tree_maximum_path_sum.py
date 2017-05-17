#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-17 14:32:25

# https://leetcode.com/problems/binary-tree-maximum-path-sum/#/description
# TODO 还有待优化，deep有缓存了，但是 get_max_path 没有用缓存


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_node_max_deep(self, node):
        """返回本node最长的deep"""
        if node is None:
            return 0
        if hasattr(node, 'deep'):
            return node.deep
        node.left_deep = self.get_node_max_deep(node.left)
        node.right_deep = self.get_node_max_deep(node.right)
        node.deep = max(node.left_deep+node.val, node.right_deep+node.val, node.val)
        return node.deep

    def get_max_path_with_node(self, node):
        """获得通过这个node的最大路径"""
        if hasattr(node, 'max_path'):
            return node.max_path
        left_deep = self.get_node_max_deep(node.left)
        right_deep = self.get_node_max_deep(node.right)
        max_path = max(left_deep, 0) + max(right_deep, 0) + node.val
        node.max_path = max_path
        return node.max_path

    def get_max_path(self, node):
        """获取最大路径"""
        if node is None:
            return 0
        paths = [self.get_max_path_with_node(node)]
        if node.right:
            paths.append(self.get_max_path(node.right))
        if node.left:
            paths.append(self.get_max_path(node.left))
        return max(paths)

    def maxPathSum(self, root):
        return self.get_max_path(root)


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
s = Solution()
print("应该是6: ")
print(s.maxPathSum(a))
a = TreeNode(-3)
print("应该是-3: ")
print(s.maxPathSum(a))
