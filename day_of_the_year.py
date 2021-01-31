#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-04-04 08:39:12


import datetime


class Solution:

    def dayOfYear(self, date):
        year, month, day = [int(x) for x in date.split("-")]
        date = datetime.date(year, month, day)
        return (date - datetime.date(year,1,1)).days + 1



solution = Solution()
print(solution.dayOfYear("2019-02-10"))
