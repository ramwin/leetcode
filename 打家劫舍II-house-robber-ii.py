# 执行用时： 36 ms , 在所有 Python3 提交中击败了 83.86% 的用户
# 内存消耗： 14.8 MB , 在所有 Python3 提交中击败了 68.89% 的用户


class Solution:
    def rob(self, nums):
        print(f"准备抢劫 {nums}")
        self.nums = nums
        self.caches = {}
        return max(
            self.max(1, len(self.nums)),
            nums[0] + self.max(2, len(self.nums)-1),
        )

    def max(self, start_index, end_index):
        key = (start_index, end_index)
        if key in self.caches:
            return self.caches[key]
        gap = end_index - start_index
        if gap <= 0:
            return 0
        if gap == 1:
            return self.nums[start_index]
        if gap == 2:
            return max(self.nums[start_index], self.nums[start_index + 1])
        if gap == 3:
            return max(
                self.nums[start_index + 1],
                self.nums[start_index] + self.nums[start_index + 2],
            )
        max_value = max(
            self.max(start_index + 1, end_index),
            self.nums[start_index] + self.max(start_index + 2, end_index),
        )
        self.caches[key] = max_value
        return max_value


for nums, answer in [
        [[1, 2], 2],
        [[0, 1], 1],
    [[2, 3, 2], 3],
    [[1, 2, 3, 1], 4],
    [[0], 0],
]:
    assert Solution().rob(nums) == answer
