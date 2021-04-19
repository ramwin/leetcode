# 执行用时： 40 ms , 在所有 Python3 提交中击败了 60.40% 的用户
# 内存消耗： 14.8 MB , 在所有 Python3 提交中击败了 57.93% 的用户


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except ValueError:
                return len(nums)
