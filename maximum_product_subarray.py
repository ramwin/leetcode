#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2019-09-23 22:03:21

import pprint
# 方案1, 双重循环
"""
[2, 3, -2, 4]      product current_product
 ij           2    None    2
 i  j         6    2       6
 i     j      -12  6       -12
 i         j  -48  6       -48
    ij        3    6       3
    i   j     -6
    i      j  -24
        ij    -2
        i  j  -8
           ij 4
"""

# 方案2, 
"""
[2, 3, -2], [4]  i == 4
最大值: [2, 3, -2] 的最大值 或者 [2, 3, -2]的最大结尾的字串乘以4
[2]  最大 2, 最大的右侧子列表 2
[2, 3] [2]的最大2 或者 [2]的右侧最大(最小) 2 * 3 = 6
[2, 3] 的最大6 或者 [2, 3] 右侧的子列表 * -2 = -6
[2, 3, -2] 的最大6 或者 [2, 3, -2]的右侧最大子列表 -2 * 4 = -8
"""

# 方案3
"""
[2, 3, -2, 4] 最大值  =
[2, 3], [-2, 4] 中的最大值的一个或者
[2, 3]的尾部子列表， 和[-2, 4]的头部子列表乘积的最大值
[-1, 2, -3, 1, 2, -3] = 
[-1, 2, -3] 最大值: 6
[1, 2, -3] 最大值: 2
[-1, 2, -3] 尾部 * [1, 2, -3] 头部 = -6 * -6 = 36
"""



from functools import reduce
class Solution:
    def maxProduct1(self, nums):
        i = 0  # i代表了字串的初始位置
        j = 0  # j代表了字串的结束位置
        if len(nums) == 1:
            return nums[0]
        product = None
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)+1):
                current_product = reduce(
                    lambda x,y: x*y,
                    nums[i:j])
                if product is None:
                    product = current_product
                else:
                    product = max(product, current_product)
                print("i: {}".format(i))
                print(f"j: {j}")
                print("当前product: {}".format(product))
                print("当前current_product: {}".format(current_product))
        return product

    def maxProduct2(self, nums):
        pprint.pprint(nums)
        result = {
            # "3: {  当前array的长度
            #     "max_value": 6,
            #     "right_sub_array_max": 0,
            #     "right_sub_array_min": -12,
            # }
        }
        for i in range(1, (len(nums) + 1)):
            result[i] = self.get_array_data(i, result, nums)
        pprint.pprint(nums, indent=4)
        pprint.pprint(result, indent=4)
        return result[len(nums)]["max_value"]

    def get_array_data(self, i, result, nums):
        result_i = {}
        print("当前计算的nums产度为{}".format(i))
        if i == 1:
            result_i = {
                "max_value": nums[0],
                "right_sub_array_max": nums[0],
                "right_sub_array_min": nums[0],
            }
        else:
            current_value = nums[i-1]
            # 求right_sub_array_max
            if "right_sub_array_max" not in result[i-1]:
                import ipdb
                ipdb.set_trace()
            if result[i-1]["right_sub_array_max"] == 0:
                result_i["right_sub_array_max"] = max(
                    current_value,
                    current_value * result[i-1]["right_sub_array_min"],
                    current_value * result[i-1]["right_sub_array_max"],
                )
            elif result[i-1]["right_sub_array_max"] > 0:
                if current_value == 0:
                    result_i["right_sub_array_max"] = 0
                elif current_value > 0:
                    result_i["right_sub_array_max"] = result[i-1]["right_sub_array_max"] * current_value
                else:
                    if result[i-1]["right_sub_array_min"] == 0:
                        result_i["right_sub_array_max"] = 0
                    elif result[i-1]["right_sub_array_min"] < 0:
                        result_i["right_sub_array_max"] = result[i-1]["right_sub_array_min"] * current_value
                    else:
                        result_i["right_sub_array_max"] = current_value
            elif result[i-1]["right_sub_array_max"] < 0:
                if current_value >= 0:
                    if result[i-1]["right_sub_array_min"] >= 0:
                        result_i["right_sub_array_max"] = result[i-1]["right_sub_array_min"] * current_value
                    else:
                        result_i["right_sub_array_max"] = current_value
                elif current_value < 0:
                    result_i["right_sub_array_max"] = max([
                        result[i-1]["right_sub_array_max"] * current_value,
                        result[i-1]["right_sub_array_min"] * current_value,
                    ])
                else:
                    raise Exception

            # if (i==3):
            #     import ipdb
            #     ipdb.set_trace()
            # 求right_sub_array_min
            if result[i-1]["right_sub_array_min"] == 0:
                result_i["right_sub_array_min"] = min(
                    current_value,
                    current_value * result[i-1]["right_sub_array_min"],
                    current_value * result[i-1]["right_sub_array_max"],
                )
            elif result[i-1]["right_sub_array_min"] > 0 and current_value >= 0:
                result_i["right_sub_array_min"] = current_value
            elif result[i-1]["right_sub_array_min"] > 0 and current_value < 0:
                if result[i-1]["right_sub_array_max"] == 0:
                    result_i["right_sub_array_min"] = current_value
                elif result[i-1]["right_sub_array_max"] > 0:
                    result_i["right_sub_array_min"] = result[i-1]["right_sub_array_max"] * current_value
                else:
                    result_i["right_sub_array_min"] = current_value
            elif result[i-1]["right_sub_array_min"] < 0: # -10
                if current_value == 0:
                    result_i["right_sub_array_min"] = 0
                elif current_value > 0:
                    result_i["right_sub_array_min"] = result[i-1]["right_sub_array_min"] * current_value
                elif current_value < 0: # -2
                    if result[i-1]["right_sub_array_max"] == 0:
                        result_i["right_sub_array_min"] = current_value
                    elif result[i-1]["right_sub_array_max"] > 0:
                        result_i["right_sub_array_min"] = current_value * result[i-1]["right_sub_array_max"]
                    else: # -5
                        result_i["right_sub_array_min"] = current_value
                else:
                    raise Exception
                
            result_i["max_value"] = max([
                current_value,
                result[i-1]["max_value"],
                result[i-1]["right_sub_array_max"] * current_value,
                result[i-1]["right_sub_array_min"] * current_value,
            ])
        pprint.pprint(result_i, indent=4)
        return result_i



if __name__ == "__main__":
    # print("2,3,-2,4")
    # print(Solution().maxProduct1([2, 3, -2, 4]))
    # assert Solution().maxProduct2([2, 3, -2, 4]) == 6
    # assert Solution().maxProduct2([-2, 0, -1]) == 0
    # assert Solution().maxProduct2([-2]) == -2
    # assert Solution().maxProduct2([-4, -3]) == 12
    # assert Solution().maxProduct2([-1,-2,-9,-6]) == 108
    # assert Solution().maxProduct2([2,-5,-2,-4,3]) == 24
    # assert Solution().maxProduct2([1,0,-1,2,3,-5,-2]) == 60
    assert Solution().maxProduct2([1,-3,2,0,-1,0,-2,-3,1,2,-3,2]) == 36
