#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-01 22:01:50


"""
[2,13,3,11,5,17,7]

result = left_list + right_list
a b a c a d a e > [a a a a ] + [b c d e]
[2, 13, 3, 11, 5, 17, 7]
[       3, 11, 5, 17, 7, 13]
[              5, 17, 7, 13, 11]
[                     7, 13, 11, 17]


[2, 13, 3, 11, 5, 17]
[       3, 11, 5, 17, 13]
[              5, 17, 13, 11]
[                     13, 11, 17]

[a b c d e f g]

[a b c d e f g]
[a   b   d   e]

2
13
3
11
5
17
7
"""

class Solution:
    """
    Runtime: 60 ms, faster than 28.03% of Python3 online submissions for Reveal Cards In Increasing Order.
Memory Usage: 13.4 MB, less than 12.50% of Python3 online submissions for Reveal Cards In Increasing Order.
Next challenges:
    """
    def find_next_empty_position(self, linked_list, position, length):
        # TODO 这个函数有点差，因为每次都要循环这个链表。更好的方式，应该记录，直接能够索引到哪个位置是空的
        """include the space in position"""
        print("找到{}里面从第{}开始的空位置".format(linked_list, position))
        if linked_list[position] is None:
            return position
        position = (position+1) % length
        return self.find_next_empty_position(linked_list, position, length)

    def deckRevealedIncreasing(self, deck):
        length = len(deck)
        if length <= 2:
            deck.sort()
            return deck
        deck.sort(reverse=True)
        # print("当前deck:")
        # print(deck)
        result = [None] * length
        first = deck.pop()
        result[0] = first
        index = 1  # 当前的位置
        # print("当前result: ")
        # print(result)
        while deck:
            first_empty_position = self.find_next_empty_position(
                result,
                index,
                length
            )
            # print("第一个空位置是: {}".format(first_empty_position))
            index = self.find_next_empty_position(
                result,
                (first_empty_position + 1) % length,
                length
            )
            # print("第二个空位置是: {}".format(index))
            assert result[index] is None
            result[index] = deck.pop()
        return result


solution = Solution()
assert solution.deckRevealedIncreasing(deck=[17,13,11,2,3,5,7]) == [2,13,3,11,5,17,7]
# print(solution.deckRevealedIncreasing(deck=[1,2]))
assert solution.deckRevealedIncreasing(deck=[1,2]) == [1,2]
assert solution.deckRevealedIncreasing(deck=[1,2, 3]) == [1,3, 2]
assert solution.deckRevealedIncreasing(deck=[1,2,3,4]) == [1,3,2,4]
