#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

"""实现插入功能"""


from typing import Union


class TreeNode:
    """二叉树定义"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    """实现插入功能"""

    def __init__(self, tree_node: TreeNode):
        """
        current_location, 下一次插入时, 所属的node
        """
        self.tree_node = tree_node
        self.current_location = self.get_init_current_location(tree_node)

    @staticmethod
    def get_init_current_location(tree_node: TreeNode):
        """
        根据treenode, 返回当前有空的位置
        """
    def insert(self, value):
        """
        1. 先找到底层左侧位置, 插入
        2. 把插入的值和顶点进行替换
        """
        self.find_location()

    def find_location(self) -> tuple(TreeNode, Union['left', 'right']):
        """
        返回底层最左侧为空的位置
        如果底层满了,就是返回底层第一个节点的left
        """
