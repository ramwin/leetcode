# 执行用时: 36 ms 超过90%
# 内存消耗: 14.8 MB 超过99%

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
