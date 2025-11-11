# 实现一个单例模式
# 实现一个斐波那契数列，支持 fab[10] fab[3]
# 实现多线程factor
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data int整型一维数组
# @return int整型一维数组
#

from typing import List


class Solution:
    def bubble_sort(self , data: List[int]) -> List[int]:
        # 从0走到结尾。每次遍历后，第n大的值会出现在最后面
        for start_index in range(len(data)):
            # 后面最大的不用对比了
            for compare_index in range(0, len(data) - start_index - 1):
                left = data[compare_index]
                right = data[compare_index + 1]
                if left > right:
                    data[compare_index] = right
                    data[compare_index + 1] = left
        return data


print(Solution().bubble_sort([1,2,3,4,8,6,7,9,5,10]))
print(Solution().bubble_sort([]))
print(Solution().bubble_sort([2, 1]))
print(Solution().bubble_sort([3, 1, 2]))
print(Solution().bubble_sort([2, 3, 2]))
