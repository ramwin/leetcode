# 执行用时： 288 ms , 在所有 Python3 提交中击败了 34.01% 的用户
# 内存消耗： 18.3 MB , 在所有 Python3 提交中击败了 26.40% 的用户


class Solution:

    @staticmethod
    def solution_count(n):
        """
        C(2, N)
        1 [0] > 1
        2 [0 0] > 3
        3 [0 0 0] > 6
        4 [0 0 0 0] > 10
        """
        if n <= 0:
            return 0
        return (n + 1) * (n) // 2

    @staticmethod
    def solution_count2(n1, n2):
        """
        2 3  [0 0] 1 1 1 [0 0 0] > 12
        """
        result = (n1+1) * (n2+1)
        print(f"solution_count2 {n1} {n2}: result: {result}")
        return result

    def numSubarraysWithSum(self, nums, goal):
        print(f"nums: {nums}, goal: {goal}")
        self.length = len(nums)
        self.number_1_index = []  # [1, 5, 8]
        self.number_1_dict = {} # {1: 4, 5: 3, 8:2}
        prev_1_index = None
        for index, num in enumerate(nums):
            if num == 1:
                self.number_1_index.append(index)
                self.number_1_dict[index] = 0
                prev_1_index = index
            else:
                if prev_1_index is not None:
                    self.number_1_dict[prev_1_index] += 1
        print(f"self.number_1_index: {self.number_1_index}")
        print(f"self.number_1_dict: {self.number_1_dict}")
        solutions = 0
        if goal == 0:
            if not self.number_1_index:
                return self.solution_count(len(nums))
            if self.number_1_index:
                solutions += self.solution_count(self.number_1_index[0])
            for n in self.number_1_dict.values():
                solutions += self.solution_count(n)
        else:
            if goal > len(self.number_1_index):
                return 0
            if goal == len(self.number_1_index):
                solutions =  self.solution_count2(
                    self.number_1_index[0],
                    self.number_1_dict[self.number_1_index[-1]],
                )
                print(f"solutions: {solutions}")
                return solutions
            start = 0
            end = goal - 1
            solutions = self.solution_count2(
                self.number_1_index[0],
                self.number_1_dict[self.number_1_index[end]],
            )
            print(f"start: {start}, end: {end}")
            print(f"solutions: {solutions}")
            start = -1
            while end < len(self.number_1_index) - 1:
                start += 1
                end += 1
                solutions += self.solution_count2(
                    self.number_1_dict[
                        self.number_1_index[start]
                    ],
                    self.number_1_dict[
                        self.number_1_index[end]
                    ],
                )
                print(f"start: {start}, end: {end}")
                print(f"solutions: {solutions}")
        print(f"solutions: {solutions}")
        return solutions


for nums, goal, result in [
    [[1, 0, 1, 0, 1], 2, 4],
    [[0, 0, 0, 0, 0], 0, 15],
    [[0, 0, 0, 0, 1], 2, 0],
    [[0, 0, 0, 1, 1], 2, 4],
    [[0, 0, 1, 1, 0], 2, 6],
    [[0, 1, 1, 1, 1], 3, 3],
    [[1,1,1,1,1,0,1,1,1,1], 5, 6],
]:
    assert Solution().numSubarraysWithSum(nums, goal) == result
