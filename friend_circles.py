#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-05-12 16:29:45

# https://leetcode.com/problems/friend-circles/#/description
# 这个问题有点像算法导论里面的找到所有的群啊。每个群设置一个头头就好了，如果有两个群里面出现了同样的元素，就把两个群合并，并且群层次比较低
# 成绩 打败36.46
# 如果不考虑depth，直接等于打败 31.22
# 如果使用int,直接等于还是只打败31.22


class Student(int):
    def __init__(self, index):
        self.index = index
        self.parent = None  # 他的群爸爸
        self.depth = 1  # 他的群等级

    @property
    def ancestor(self):
        if self.parent is not None:
            return self.parent.ancestor
        else:
            return self


class Solution(object):
    def findCircleNum(self, M):
        students = {}
        for i in range(len(M)):
            students[i] = Student(i)
        for index_i, row in enumerate(M):
            for index_j, is_friend in enumerate(row):
                if index_i == index_j:
                    pass
                else:
                    if is_friend == 1:
                        if students[index_j].ancestor != students[index_i].ancestor:
                            students[index_j].ancestor.parent = students[index_i].ancestor
                            # leap = students[index_j].ancestor.depth - students[index_i].ancestor.depth
                            # if leap < 0:
                            #     students[index_j].ancestor.parent = students[index_i].ancestor
                            # elif leap > 0:
                            #     students[index_i].ancestor.parent = students[index_j].ancestor
                            # else:
                            #     students[index_i].ancestor.parent = students[index_j].ancestor
                            #     students[index_j].ancestor.depth += 1
        return len(list(filter(lambda x: x.parent is None, students.values())))


a = Solution()
print(a.findCircleNum([[1,1,1],[1,1,1],[1,1,1]]))
