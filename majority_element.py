#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-24 17:06:37


class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        major = nums[0]
        cnt = 1
        for i in nums[1:]:
            if i == major:
                cnt += 1
            else:
                if cnt == 0:
                    major = i
                    cnt = 1
                    continue
                cnt -= 1
        return major


a = Solution()
print(a.majorityElement([3,2,3]))
