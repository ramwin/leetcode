#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
完全二叉树插入器的单元测试
"""


import unittest
from base import CBTInserter


class Test(unittest.TestCase):
    """基础测试"""

    @staticmethod
    def create_tree_node():
        """创建一个二叉树"""
        node2 = TreeNode(val=2)
        node1 = TreeNode(
            val=1, left=node2
        )
        return node1

    def test(self):
        tree_node = create_tree_node()
        cbt_inserter = CBTInserter(tree_node)
        cbt_inserter.insert(
            3
        )
        self.assertEqual(
            tree_node.right.val,
            3
        )
        cbt_inserter.insert(4)
        self.assertEqual(
            tree_node.left.left.val,
            4
        )
