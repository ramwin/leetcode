# 速度超过 98.66% 内存超过35.05%（因为递归)
class Solution:

    def searchMatrix(self, matrix, target: int) -> bool:
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        return self.find(matrix, 0, self.rows * self.columns - 1, target)

    def find(self, matrix, left, right, target):
        if right - left == 1:
            return self.index(matrix, left) == target or self.index(matrix, right) == target
        if left == right:
            return self.index(matrix, left) == target
        if self.index(matrix, (left+right) // 2) > target:
            return self.find(matrix, left, (left+right) // 2, target)
        else:
            return self.find(matrix, (left+right) // 2, right, target)

    def index(self, matrix, index):
        x, y = index // self.columns, index % self.columns
        return matrix[x][y]


# 速度超过83.96% 内存超过98.48%
class Solution:

    def searchMatrix(self, matrix, target: int) -> bool:
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        left = 0
        right = self.rows * self.columns - 1
        while right - left > 1:
            half = (right + left) // 2 
            if self.index(matrix, half) > target:
                right = half
            else:
                left = half
        return self.index(matrix, left) == target or self.index(matrix, right) == target

    def index(self, matrix, index):
        x, y = index // self.columns, index % self.columns
        print(f"{index} => {x}, {y}")
        return matrix[x][y]


s = Solution()
for matrix, target, result in (
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True,),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False,),
    ([[1,1]], 0, False),
    ([[1]], 0, False),
):
    assert(s.searchMatrix(matrix, target) == result)


