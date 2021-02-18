#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 看错题目了, 题目规定只交换一个. 我这解法可以交换任意个
# 难怪题目是简单版本了

class Candy:

    def __init__(self, source, size):
        self.source = source
        self.size = size
        self.current = None

    def __repr__(self):
        return f"{self.source.name}: {self.size}"


class Person:

    def __init__(self, candies, name):
        self.candies = set()
        self.size = 0
        self.name = name
        for candy in candies:
            self.candies.add(
                Candy(self, candy)
            )

    def add_candy(self, candy):
        candy.current = self
        self.size += candy.size
        self.candies.add(candy)

    @property
    def not_mine_cnt(self):
        cnt = 0
        for candy in self.candies:
            if candy.source == self:
                continue
            else:
                cnt += candy.size
        return cnt

    def give_candy(self, candy, target):
        target.add_candy(candy)
        self.candies.remove(candy)
        self.size -= candy.size

    def __repr__(self):
        return f"{self.name}: {self.candies}"


class Solution:
    def fairCandySwap(self, A, B):
        alice = Person([], name="alice")
        bob = Person([], name="bob")
        all_candies = []
        for size in A:
            all_candies.append(
                Candy(source=alice, size=size)
            )
        for size in B:
            all_candies.append(
                Candy(source=bob, size=size)
            )
        all_candies.sort(key=lambda x: x.size, reverse=True)
        print(all_candies)

        for candy in all_candies:
            if alice.size > bob.size:
                bob.add_candy(candy)
            else:
                alice.add_candy(candy)
        print(alice)
        print(bob)

        diff = bob.size - alice.size
        if diff == 0:
            print("gotcha")
            result = [bob.not_mine_cnt, alice.not_mine_cnt]
            print(result)
            return result

        exchange_methods = {
            diff: set(),
        }
        for candy in all_candies[::-1]:
            for diff, candies in exchange_methods.items():
                if candy.current == bob:
                    exchange_methods[diff-candy*2] == candies | {candy}
                if candy.current == alice:
                    exchange_methods[diff+candy*2] == candies | {candy}
            for candy in exchange_methods:
                if candy.current == alice:
                    candy.current.give_candy(candy, bob)
                else:
                    candy.current.give_candy(candy, alice)
            return [bob.not_mine_cnt, alice.not_mine_cnt]


s = Solution()
# assert s.fairCandySwap([1, 1], [2, 2]) == [1, 2]
assert s.fairCandySwap([1, 2, 5], [2, 4]) == [5, 4]
