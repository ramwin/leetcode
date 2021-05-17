# 执行用时： 48 ms , 在所有 Python3 提交中击败了 28.83% 的用户
# 内存消耗： 14.8 MB , 在所有 Python3 提交中击败了 73.76% 的用户


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def create_from_list(cls, array):
        tree_nodes = list(
            cls(val=number)
            for number in array
        )
        for index, tree_node in enumerate(tree_nodes):
            try:
                tree_node.left = tree_nodes[index * 2 + 1]
                tree_node.right = tree_nodes[index * 2 + 2]
            except IndexError:
                return tree_nodes[0]
        return tree_nodes[0]


class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val in [x, y]:
            return False
        parents = [root]
        while parents:
            values = self.get_child_values(parents)

            if x in values and y in values:
                return values[x] != values[y]
            elif x not in values and y not in values:
                parents = self.get_parensts(parents)
                continue
            else:
                return False

    def get_parensts(self, parents):
        result = []
        for parent in parents:
            if parent.left:
                result.append(parent.left)
            if parent.right:
                result.append(parent.right)
        return result

    def get_child_values(self, parents):
        result = {}
        for parent in parents:
            if parent.left:
                result[parent.left.val] = parent
            if parent.right:
                result[parent.right.val] = parent
        return result


assert Solution().isCousins(
    TreeNode.create_from_list([1, 2, 3, None, 4, None, 5]),
    4, 3) is False
