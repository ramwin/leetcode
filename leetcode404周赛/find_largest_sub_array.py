#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import logging
from typing import List



logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


class Solution:
    """
    nums = [1,4,2,3,1,4], k = 3
    nums = [1, 1, 2, 0, 1, 1]
    1, 1 == 
    1, 2 
    # nums2 =[  2  0  2  1  2 ]
    """

    def maximumLength(self, nums: List[int], k: int) -> int:  # pylint: disable=invalid-name
        if len(nums) < 2:
            raise ValueError("说好的>=2呢")
        if len(nums) == 2:
            return 2
        divid_nums = [ ]
        for index in range(len(nums) - 1):
            divid_nums.append(
                    (nums[index] + nums[index+1]) % k
            )
        LOGGER.info("取余后的结果是: %s", divid_nums)
        cur_max = 0
        cur_len = 1
        start_index = 0
        same_value = divid_nums[start_index]
        for num in divid_nums[1:]:
            if num == same_value:
                cur_len += 1
            else:
                cur_max = max(cur_len, cur_max)
                cur_len = 1
                same_value = num
        cur_max = max(cur_len, cur_max)
        return cur_max + 1
