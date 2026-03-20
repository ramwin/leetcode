class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        """
        使两个二进制字符串相等的最小操作成本
        
        操作1: 翻转s1[i]和s1[j]，成本x
        操作2: 翻转s1[i]和s1[i+1]，成本1
        
        思路:
        1. 找出所有s1和s2不同的位置diff
        2. 如果diff数量为奇数，无法配对，返回-1
        3. 使用区间DP计算最小成本
           - dp[l][r]表示配对diff[l..r]中所有位置的最小成本
           - 配对diff[l]和diff[k]的成本: 连续则为1，否则min(x, diff[k]-diff[l])
        """
        # 找到所有不同的位置
        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]
        m = len(diff)
        
        # 如果不同位置数量为奇数，无法配对，返回-1
        if m % 2 == 1:
            return -1
        
        if m == 0:
            return 0
        
        # 区间DP: dp[l][r] 表示处理 diff[l..r] 的最小花费
        # 注意：区间长度必须是偶数才有解
        INF = float('inf')
        dp = [[0] * m for _ in range(m)]
        
        # 初始化：相邻两个配对
        for i in range(m - 1):
            # 如果连续，花费1（使用操作2）；否则 min(x, 距离)
            if diff[i+1] == diff[i] + 1:
                dp[i][i+1] = 1
            else:
                dp[i][i+1] = min(x, diff[i+1] - diff[i])
        
        # 处理更长的区间，长度从4开始，每次增加2（保证偶数长度）
        for length in range(4, m + 1, 2):
            for l in range(0, m - length + 1):
                r = l + length - 1
                dp[l][r] = INF
                # 枚举diff[l]和谁配对（必须是奇数位置距离，保证中间有偶数个）
                for k in range(l + 1, r + 1, 2):
                    # 配对diff[l]和diff[k]的花费
                    if diff[k] == diff[l] + 1:
                        cost_lk = 1
                    else:
                        cost_lk = min(x, diff[k] - diff[l])
                    
                    # 中间区间[l+1, k-1]的花费
                    middle = dp[l+1][k-1] if k > l + 1 else 0
                    # 右边区间[k+1, r]的花费
                    right = dp[k+1][r] if k < r else 0
                    
                    dp[l][r] = min(dp[l][r], cost_lk + middle + right)
        
        return dp[0][m-1]


# 测试代码
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    s1 = "1100011000"
    s2 = "0101001010"
    x = 2
    print(f"Example 1: {sol.minOperations(s1, s2, x)}")  # Expected: 4
    
    # Example 2
    s1 = "10110"
    s2 = "00011"
    x = 4
    print(f"Example 2: {sol.minOperations(s1, s2, x)}")  # Expected: -1
    
    # 测试你提到的反例
    s1 = "0100011001"  # diff = [1,5,6,9]
    s2 = "0000000000"
    x = 100
    print(f"Test case [1,5,6,9] with x=100: {sol.minOperations(s1, s2, x)}")  # Expected: 7
    
    # 新测试用例（用户提供的错误测试）
    s1 = "1110111001000001"
    s2 = "0110011110101101"
    x = 1
    result = sol.minOperations(s1, s2, x)
    print(f"Test case x=1: {result}")  # Expected: 4
    
    # 验证diff
    diff = [i for i in range(len(s1)) if s1[i] != s2[i]]
    print(f"  diff positions: {diff}")  # Should be [0, 4, 7, 8, 9, 10, 12, 13]
    print(f"  expected: {len(diff) // 2}")  # When x=1, each pair costs 1
