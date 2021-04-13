from decimal import Decimal


# 执行用时： 40 ms , 在所有 Python3 提交中击败了 70.68% 的用户
# 内存消耗： 14.8 MB , 在所有 Python3 提交中击败了 83.18% 的用户

class Solution:

    def minDiffInBST(self, root):
        if root is None:
            return Decimal("inf")
        compare_values = [
            self.minDiffInBST(root.left),
            self.minDiffInBST(root.right),
        ]
        if root.right:
            compare_values.append(
                self.get_min(root.right) - root.val,
            )
        if root.left:
            compare_values.append(
                root.val - self.get_max(root.left)
            )
        return min(compare_values)

    def get_max(self, root):
        if not root.right:
            return root.val
        return self.get_max(root.right)

    def get_min(self, root):
        if not root.left:
            return root.val
        return self.get_min(root.left)
