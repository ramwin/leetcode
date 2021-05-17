import math


class Solution:

    def largestDivisibleSubset(self, nums):
        nums.sort()
        if nums[0] == 1:
            return [1] + self.largestDivisibleSubset(nums[1:])
        if not nums:
            return []
        self.start_index = 0  # 第一个元素可能的最左位置
        self.current_index = 0
        results = [nums[0]]
        while True:
            self.current_index += 1
            if int(math.log(nums[-1], nums[self.current_index])) < len(results):
                break


s = Solution()
print(s.largestDivisibleSubset([1,2,3]))
print(s.largestDivisibleSubset([1,2,4,8]))
