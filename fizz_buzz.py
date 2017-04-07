#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-04-07 18:14:03


class Solution(object):

    def fizzBuzz(self, n):
        results = []
        for i in range(1, n+1):
            if i%15==0:
                results.append('FizzBuzz')
            elif i%3 == 0:
                results.append('Fizz')
            elif i%5 == 0:
                results.append('Buzz')
            else:
                results.append(str(i))
        return results
