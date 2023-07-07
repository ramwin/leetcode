#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def create_from_list(cls, array: List[int]):
        """

        level0: [               10,
        level1:      5,                   -3,
        level2:    3,      2,          null, 11,
        level3: 3,   -2, null, 1]
        """
        level = 0  # 当前处理了多少层
        root = TreeNode(val=array[0])
        pre_level_nodes = [root]
        current_level_nodes = [root]
        while True:
            pre_level_nodes = current_level_nodes
            current_level_nodes = []
            level += 1
            for i in range(2 ** level):
                index = 2 ** level - 1 + i
                if index >= len(array):
                    return root
                if array[index] is None:
                    continue
                node = TreeNode(val=array[index])
                current_level_nodes.append(node)
                parent = pre_level_nodes[i // 2]
                if i % 2 == 0:
                    parent.left = node
                else:
                    parent.right = node
