class Solution:

    def numDecodings(self, s):
        total = 0

    @classmethod
    def can_decode(cls, s):
        if len(s) == 0:
            return False
        if s[0] == "0":
            return False
        return int(s) <= 26
