#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-31 13:54:56


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        if n == 2:
            return max(prices[1] - prices[0], 0)
        else:
            return max(
                Solution().maxProfit(prices[0:n//2]),
                Solution().maxProfit(prices[n//2:n]),
                max(prices[n//2:n]) - min(prices[0:n//2])
                )
        return b-a

