
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 46.10% 的用户
# 内存消耗： 15.7 MB , 在所有 Python3 提交中击败了 93.22% 的用户

class Solution:

    def removeDuplicates(self, nums):
        n = len(nums) - 1
        while n >= 1:
            if nums[n] == nums[n-1]:
                nums.pop(n)
            n -= 1
        return len(nums)


s = Solution()
a = [1, 1, 2]
assert s.removeDuplicated(a) == 2
assert a == [1, 2]
b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
assert s.removeDuplicated(b) == 5
assert b == [0, 1, 2, 3, 4]
c = [1]
assert s.removeDuplicated(c) == 1
assert c == [1]
