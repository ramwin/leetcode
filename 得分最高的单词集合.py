#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>

"""
得分最高的单词集合

你将会得到一份单词表 words，一个字母表 letters （可能会有重复字母），以及每个字母对应的得分情况表 score。

请你帮忙计算玩家在单词拼写游戏中所能获得的「最高得分」：能够由 letters 里的字母拼写出的 任意 属于 words 单词子集中，分数最高的单词集合的得分。

单词拼写游戏的规则概述如下：

玩家需要用字母表 letters 里的字母来拼写单词表 words 中的单词。
可以只使用字母表 letters 中的部分字母，但是每个字母最多被使用一次。
单词表 words 中每个单词只能计分（使用）一次。
根据字母得分情况表score，字母 'a', 'b', 'c', ... , 'z' 对应的得分分别为 score[0], score[1], ..., score[25]。
本场游戏的「得分」是指：玩家所拼写出的单词集合里包含的所有字母的得分之和。
 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-score-words-formed-by-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Word:
    """单词的对象"""

    def __init__(self, word, index):
        self.word = word
        self.index = index  # 单词的索引
        self.score = 0  # 单词的分数


class Solution1:
    """

    执行用时： 40 ms , 在所有 Python3 提交中击败了 100.00% 的用户
    内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 33.33% 的用户

    思路一:
    把words的所有子集挑选出来, 看子集是否能用所有letters进行表示, 找到分数最高的子集
    耗时 2 ^ (words长)  = 2 ^ 14
    [w1, w2, w3], [w4]
    最长 = [w1, w2, w3]分数 + [w1, w2, w3] 用去掉w4构成的分数 + w4的分数
        难点: 动态规划要想速度快, 必须有缓存.
              letters子集来生成缓存
        常用函数:
            从letters取出一部分后计算
            计算已有word的分数
    """

    def __init__(self, words, letters, score):
        """
        score: 26个字母的值
        """
        self.letters = letters
        self.score_dict = {
            chr(i): score[i-ord('a')]
            for i in range(ord('a'), ord('z')+1)
        }
        self.word_instances = [
            self.create_word_instance(word, index)
            for index, word in enumerate(words)
        ]

    def create_word_instance(self, word, index):
        """把一个单词变成对象,加入Solution"""
        word = Word(word, index)
        word.score = self.get_score(word.word)
        return word

    def get_score(self, word):
        """获取一个单词word的分值"""
        result = 0
        for letter in word:
            result += self.score_dict[letter]
        return result

    def get_max_score(self, words, letters):
        """
        获取用letters拼接成words的最高分
        要么, 不需要最后一个word
        要么, 需要最后一个word,
        """
        if not words:
            return 0
        score_without_last = self.get_max_score(
            words[0: -1], letters
        )
        remain_letters = self.get_remain_letters(
            words[-1].word, letters
        )
        if remain_letters is not None:
            score_with_last = self.get_max_score(
                words[0: -1], remain_letters,
            ) + words[-1].score
        else:
            score_with_last = 0
        return max(
            score_without_last, score_with_last
        )

    def get_remain_letters(self, word, letters):
        """
        从letters里面挑选出字母, 构成word
        返回剩下的letters.
        如果无法构成word, 返回None
        """
        letters = letters.copy()
        for letter in word:
            try:
                letters.remove(letter)
            except ValueError:
                return None
        return letters


class Solution2:
    """
    思路二:
    把letters所能构成的所有子集找出来.
    看这个子集的最高分
    因为letters只有100个, 用动态规划
    [a, b, c], [d] 构成了 ac. 这时候d是否要放入
    是否要拆掉ac呢.
    """


class Solution:
    """兼容题目"""
    def maxScoreWords(self, words, letters, score):
        """返回最大分"""
        solution = Solution1(
            words, letters, score
        )
        return solution.get_max_score(
            solution.word_instances,
            solution.letters,
        )
