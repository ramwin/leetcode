#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-08-01 14:41:10

# https://leetcode.com/problems/decode-ways/description/

# TODO

global debug
debug = False


class Solution:

    @property
    def debug(self):
        return True  # if you don't want to debug, change the True to False

    def validate(self, s):
        """check if it should return 0 or not"""
        if s[0] == '0':
            if self.debug:
                print("{} cannot be decoded that startswith '0'".format(s))
            return 0
        if '00' in s:
            if self.debug:
                print("string with '00' cannot be decoded")
            return 0
        if hasattr(self, 'notinit'):
            pass
        else:
            self.notinit = True
            for i in s.split('0')[0:-1]:
                if self.debug:
                    print(s.split('0'))
                if i[-1] not in ['1', '2']:
                    if self.debug:
                        print("the digital before '0' should be '1' or '2'")
                    return 0
        self.is_valid = True
        return None

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 12123
        # 12 123  vs  1 21 23
        # there is two kind choice, the letter break between 2 and 1 or the letter don't break between 2 and 1.
        # the later one is enable only if the 21 can be decoded (less than 26)
        # total = numDecodings('12') * numDecodings('123') + [ numDecodings('1') * numDecodings('23') ]
        # attention a single zero can't be decoded. so if you encounter 0 like 11042, you must split it into 1 10 42 three part
        # if hasattr(self, 'is_valid'):
        #     pass
        # else:
        #     result = self.validate(s)
        #     if result is not None:
        #         return result
        # TODO I want to just validate the firsttime, but it looks leetcode is using the same solution. You can create a new method in the class to avoid check is_valid everytime
        result = self.validate(s)
        if result is not None:
            return result
        if len(s) == 0:
            return 0
        if self.debug:
            print("处理{}".format(s))
        if not s:
            raise Exception("{} is empty".format(s))
        if not int(s):
            raise Exception("{} is only zero".format(s))
        if len(s) == 1:
            # print('"{}" only have one explain'.format(s))
            return 1
        if len(s) == 2:
            if s[1] == '0':  # 10 can only be decoded as 10
                return 1
            if int(s) <= 26:  # 12, 13 have two solution
                return 2
            else:
                return 1
        if len(s) == 3:
            if '0' in s:
                return 1
            else:
                num = 1  # 'a' 'b' 'c'
                if int(s[0:2]) <= 26:  # 'ab', 'c'
                    num += 1
                if int(s[1:3]) <= 26:  # 'a', 'bc'
                    num += 1
                return num
        if s[-1] == '0':  # '1120' => '11' '20'
            return self.numDecodings(s[:-2])
        break_position = len(s)//2
        if s[break_position] == '0':  # '112|0211' => '1120' '211' 0 can't be the start of a string
            # print("{}'s right part startwith zero")
            break_position += 1
            if self.debug:
                print("{}'s right part start with zero".format(s))
            return self.numDecodings(s[0:break_position]) * self.numDecodings(s[break_position:])
        else:  # '1121211' => '123' * '456' + '12' * '56' (if 34 is valid)
            if s[break_position+1] == '0':  # if it is 123 and 406
                return self.numDecodings(s[0:break_position]) * self.numDecodings(s[break_position+2:])
            else:  # if it is 123 and 456
                if s[break_position-1] != '0' and int(s[break_position-1:break_position+1]) <= 26:  # if 34 can be decoded
                    return self.numDecodings(s[:break_position-1]) * self.numDecodings(s[break_position+1:]) + \
                        self.numDecodings(s[:break_position]) * self.numDecodings(s[break_position:])
                else:  # if 34 can't be decoded
                    return self.numDecodings(s[:break_position]) * self.numDecodings(s[break_position:])

test_data = {
    '0': 0,
    '0600': 0,
    '12': 2,
    '226': 3,
    '1111': 5,
    '1101': 1,
    '1017': 2,
    '301': 0,
    '100': 0,
}
for key, value in test_data.items():
    s = Solution()
    result = s.numDecodings(key)
    if result != value:
        debug = True
        if s.debug:
            print("{} has {} choice，but the computed result is {}".format(key, value, result))
