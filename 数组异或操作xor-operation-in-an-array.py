# 执行用时： 36 ms , 在所有 Python3 提交中击败了 82.37% 的用户
# 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了 13.77% 的用户

import functools
import operator
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(
            operator.xor,
            [
            start + 2 * i
            for i in range(n)
        ])
