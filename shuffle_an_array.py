#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-17 15:21:51

import random
class Solution(object):
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)
    def reset(self):
        return self.nums
    def shuffle(self):
        return random.sample(self.nums, self.length)
