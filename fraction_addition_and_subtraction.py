#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-23 15:42:04


# https://leetcode.com/problems/fraction-addition-and-subtraction/#/description


from fractions import Fraction
import unittest


class Solution(object):
    def fractionAddition(self, expression):
        numbers = expression.split('+')
        result = Fraction(0,1)
        for number in numbers:
            if number == '':
                continue
            for index, j in enumerate(number.split('-')):
                if '/' in j:
                    value = Fraction(*map(int, j.split('/')))
                else:
                    value = int(j or '0')
                if index == 0:
                    result += value
                else:
                    result -= value
            print("number: %s" % number)
            print("value: %s" % value)
            print("result: %s" % result)
        return "%d/%d" % (result.numerator, result.denominator)


class Test(unittest.TestCase):
    def testsolution(self):
        s = Solution()
        self.assertEqual(s.fractionAddition('-1/2+1/2+1/3'), '1/3')


if __name__ == '__main__':
    unittest.main()
