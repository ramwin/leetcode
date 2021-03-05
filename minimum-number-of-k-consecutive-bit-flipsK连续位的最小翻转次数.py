
from collections import deque
# 第一次, 超时,K很大

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


# 第二次, 用一个列表来记录前面的反转次数

class Solution:

    def minKBitFlips(self, A, K) -> int:
        self.A = A
        self.current_index = 0
        self.K = K
        self.K_list = list(range(K))
        self.total = 0
        self.rotate_queues = deque()
        final_index = len(A) - K

        while True:
            try:
                self.left_rotate()
            except ValueError:
                return self.total

    def left_rotate(self):
        print(f"{self.A} rotate at {self.current_index}")
        self.rotate_queues.append(self.current_index)
        self.current_index = self.A.index(0, self.current_index+1)
        print(f"索引走到了 {self.current_index}")
        while self.rotate_queues and self.rotate_queues[0] + self.K < self.current_index:
            self.rotate_queues.popleft()
        print(f"{self.rotate_queues}")
        self.total += 1


for A, K, answer in [
        [[0, 1, 0], 1, 2],
        [[1, 1, 0], 2, -1],
        [[0,0,0,1,0,1,1,0], 3, 3],
]:
    assert Solution().minKBitFlips(A, K) == answer
