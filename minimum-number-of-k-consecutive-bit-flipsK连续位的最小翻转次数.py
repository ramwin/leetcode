
# 第一次

class Solution:

    def minKBitFlips(self, A, K) -> int:
        self.A = A
        self.K = K
        self.K_list = list(range(K))
        self.total = 0
        self.pop()
        if not self.A:
            return 0
        while self.A and len(self.A) >= K:
            self.left_rotate()
            self.pop()
        if self.A:
            return -1
        return self.total

    def pop(self):
        # print(f"{self.A} pop", end=": ")
        while self.A and self.A[0] == 1:
            self.A.pop(0)
        # print(f"{self.A}")

    def left_rotate(self):
        self.total += 1
        for index in self.K_list:
            if self.A[index] == 1:
                self.A[index] = 0
            else:
                self.A[index] = 1


for A, K, answer in [
        [[0, 1, 0], 1, 2],
        [[1, 1, 0], 2, -1],
        [[0,0,0,1,0,1,1,0], 3, 3],
]:
    assert Solution().minKBitFlips(A, K) == answer
