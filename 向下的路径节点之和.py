#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

"""
https://leetcode.cn/problems/6eUYwP/
"""


from tree_node import TreeNode


class MySolution1:
    """
    根节点, 找到路径求和为sum_number的数量 =
        1. 根节点的左节点(可不包含)的路径求和为sum_number的数量
        2. 含根节点的左节点的路径求和为sum_number - number_root的数量
        3. 根节点的右节点(可不包含)的路径求和为sum_number的数量
        4. 含根节点的右节点的路径求和为sum_number - number_root的数量

    执行用时： 588 ms , 在所有 Python3 提交中击败了 18.00% 的用户
    内存消耗： 51.8 MB , 在所有 Python3 提交中击败了 5.00% 的用户

    """

    def __init__(self, root, target_sum, include=False):
        """
        include: 路径里是否必须包含根节点
        """
        self.root = root
        self.target_sum = target_sum
        self.include = include

    def get_result(self):
        if self.root is None:
            return 0
        # 尝试了只有include才加缓存, 没什么效果
        if self.include:
            cache_key = "_cache_include"
        if not hasattr(self.root, cache_key):
            setattr(self.root, cache_key, {})
        cache_data = getattr(self.root, cache_key)
        if self.target_sum in cache_data:
            return cache_data[self.target_sum]

        if self.root.val == self.target_sum:
            number = 1
        else:
            number = 0
        if self.include is False:
            if self.root.left:  # number1
                number += MySolution1(
                    self.root.left,
                    self.target_sum
                ).get_result()
            if self.root.right:  # number3
                number += MySolution1(
                    self.root.right,
                    self.target_sum
                ).get_result()
        # number2
        if self.root.left:
            number += MySolution1(
                self.root.left,
                self.target_sum - self.root.val,
                include=True,
            ).get_result()
        # number4
        if self.root.right:
            number += MySolution1(
                self.root.right,
                self.target_sum - self.root.val,
                include=True,
            ).get_result()

        cache_data[self.target_sum] = number
        return number


class MySolution2:
    """
    MySolution1的逆向思维. 对于每个子节点, 判断
    往上多少个节点能否求和得到某个值. 每个子节点, 保存
    从自己往上开始所有的求和可能性.
    对此我们
    """

    def __init__(self, root, target_sum):
        self.root = root
        self.target_sum = target_sum

    def get_result(self):
        result = 0
        for leaf_node in self.iter_nodes():
            result += self.get_target(
                leaf_node, self.target_sum)

    def iter_nodes(self):
        """返回所有的节点"""

    def get_target(self, node, target_sum):
        """
            返回以node为底部第一个元素, 求和得到target_sum的路径数"""


class Solution:
    """模板"""
    def pathSum(self, root: TreeNode,
                targetSum: int) -> int:
        return MySolution1(root, targetSum).get_result()


if __name__ == "__main__":
    test_root = TreeNode.create_from_list(
        [10,5,-3,3,2,None,11,3,-2,None,1])
    print(Solution().pathSum(test_root, 8))
