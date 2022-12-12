#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import dataclasses
import logging


DEBUG = True

if DEBUG:
    level = logging.DEBUG
else:
    level = logging.ERROR

stream_handler = logging.StreamHandler()

logging.basicConfig(
    level=level,
    format=(
        '[line:%(lineno)3d] %(message)s'
    ),
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        stream_handler,
    ],
)
logger = logging.getLogger(__name__)


if DEBUG:

    @dataclasses.dataclass
    class TreeNode:
        """节点"""
        val: int
        left: int = None
        right: int = None


@dataclasses.dataclass
class Slice:
    """切片, 包括left, 不包括right"""
    left: int
    right: int


class Solution1:
    """
    构建 inorder 的dict, 能够通过Preorder的首节点,把inorder区分成左侧和右侧的两个列表

    执行用时： 76 ms , 在所有 Python3 提交中击败了 71.22% 的用户
    内存消耗： 23.5 MB , 在所有 Python3 提交中击败了 61.69% 的用户

    """

    def __init__(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        self.value_dict = {
            value: index
            for index, value in enumerate(inorder)
        }
        # breakpoint()
        self.root = self.get_node(
            Slice(0, len(self.preorder)),
            Slice(0, len(self.inorder)),
        )

    def get_node(self, preorder_slice, inorder_slice, level=0):
        """
        [20, 15, 7]
        [15, 20, 7]
        根据2个列表, 生成一个node
        """
        logger.debug("%s 获取 inorder_slice 的节点: %s", " " * level, inorder_slice)

        if preorder_slice.left >= preorder_slice.right:
            return None

        node = TreeNode(val=self.preorder[preorder_slice.left])
        node_index = self.value_dict[node.val]

        # 左侧节点
        left_node_cnt = node_index - inorder_slice.left
        logger.debug("%s %s 左侧节点有 %d 个", " " * level, node, left_node_cnt)
        if left_node_cnt == 0:
            left_node = None
        else:
            left_node_slice = (
                Slice(
                    preorder_slice.left + 1,
                    preorder_slice.left + 1 + left_node_cnt,
                ),
                Slice(
                    left=node_index - left_node_cnt,
                    right=node_index,
                ),
            )
            left_node = self.get_node(
                *left_node_slice,
                level=level+1,
            )
        logger.debug("%s %s 左侧是 [%d]: %s", " " * level, node, level + 1, left_node)
        node.left = left_node

        # 右侧节点
        right_node_cnt = inorder_slice.right - node_index - 1
        if right_node_cnt == 0:
            right_node = None
        else:
            right_node_slice = (
                Slice(
                    preorder_slice.right - right_node_cnt,
                    preorder_slice.right
                ),
                Slice(
                    node_index+1,
                    inorder_slice.right,
                )
            )
            right_node = self.get_node(
                *right_node_slice,
                level=level+1,
            )
        node.right = right_node
        logger.debug("%s %s 右侧是 [%d]: %s", " " * level, node, level + 1, right_node)

        return node


class Solution:
    """兼容题目"""
    def buildTree(self, preorder, inorder):
        return Solution1(preorder, inorder).root
