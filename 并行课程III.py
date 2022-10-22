#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


"""
给你一个整数 n ，表示有 n 节课，课程编号从 1 到 n 。同时给你一个二维整数数组 relations ，
其中 relations[j] = [prevCoursej, nextCoursej] ，表示课程 prevCoursej 必须在课程 nextCoursej 之前 完成（先修课的关系）。
同时给你一个下标从 0 开始的整数数组 time ，其中 time[i] 表示完成第 (i+1) 门课程需要花费的 月份 数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/parallel-courses-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import logging
import heapq
from decimal import Decimal
from typing import List


class Course:
    """课程对象"""

    def __init__(self, _id, cost: int, end_time=Decimal('inf')):
        """
        cost: 课程需要花费的月份数
        """
        self._id = _id
        self.cost = cost
        self.end_time = end_time  # 默认
        self.prev = set()  # 保存的是Course对象
        self.next = set()  # prev和next随着时间的流逝会pop

    def __lt__(self, other):
        return self.end_time < other.end_time

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return self._id


class Solution1:
    """
    模拟现实状况. 死循环, 每次时间跳转到最近完成的课程, 把最近完成的课程加入学习队列
    执行用时： 676 ms , 在所有 Python3 提交中击败了 5.47% 的用户
    内存消耗： 68.5 MB , 在所有 Python3 提交中击败了 22.65% 的用户
    """

    def __init__(self, relations, times):
        self.course_dict = self.create_course(times)
        self.init_relations(relations)
        # 每次都要pop最近完成的课程
        self.current_learning = self.init_start_learning_courses()
        self.time = 0

    def get_result(self):
        while self.current_learning:
            first_end_course = heapq.heappop(self.current_learning)
            self.time = first_end_course.end_time
            for next_course in first_end_course.next:
                next_course.prev.remove(first_end_course)
                if not next_course.prev:
                    next_course.end_time = self.time + next_course.cost
                    heapq.heappush(
                        self.current_learning,
                        next_course,
                    )
        return self.time

    def create_course(self, times):
        """创建所有课程"""
        course_dict = {
        }
        for index, time in enumerate(times):
            course_dict[index+1] = Course(
                _id=index+1,
                cost=time,
            )
        return course_dict

    def init_relations(self, relations):
        for pre_id, next_id in relations:
            self.course_dict[pre_id].next.add(
                self.course_dict[next_id]
            )
            self.course_dict[next_id].prev.add(
                self.course_dict[pre_id]
            )

    def init_start_learning_courses(self):
        """找到所有没有依赖的课程, 加入current_learning"""
        results = []
        for course in self.course_dict.values():
            if not course.prev:
                course.end_time = course.cost
                results.append(course)
        heapq.heapify(results)
        return results


class Solution2:
    """
    递归. 每个课程的完成时间, 等于课程时间+前置依赖的课程的完成时间

    执行用时： 836 ms , 在所有 Python3 提交中击败了 5.47% 的用户
    内存消耗： 156 MB , 在所有 Python3 提交中击败了 5.46% 的用户

    """

    def __init__(self, relations, times):
        self.course_dict = self.create_course(times)
        self.init_relations(relations)
        # 每次都要pop最近完成的课程

    def get_result(self):
        end_time = 0
        for course in self.course_dict.values():
            if course.end_time is None:
                course.end_time = self.get_end_time(course)
            if course.end_time > end_time:
                end_time = course.end_time
        return end_time

    def get_end_time(self, course) -> int:
        """
        递归地获取课程的结束时间
        """
        if course.end_time is not None:
            return course.end_time
        if not course.prev:
            course.end_time = course.cost
            return course.cost
        course.end_time = max((
            self.get_end_time(course)
            for course in course.prev
        )) + course.cost
        return course.end_time

    def create_course(self, times):
        """创建所有课程"""
        course_dict = {
        }
        for index, time in enumerate(times):
            course_dict[index+1] = Course(
                _id=index+1,
                cost=time,
                end_time=None
            )
        return course_dict

    def init_relations(self, relations):
        for pre_id, next_id in relations:
            self.course_dict[pre_id].next.add(
                self.course_dict[next_id]
            )
            self.course_dict[next_id].prev.add(
                self.course_dict[pre_id]
            )


class Course3:
    """课程对象"""

    def __init__(self, _id, cost: int, end_time=Decimal('inf')):
        """
        cost: 课程需要花费的月份数
        """
        self._id = _id
        self.cost = cost
        self.end_time = end_time  # 默认
        self.prev = set()  # 保存的是Courseid
        self.next = set()  # prev和next随着时间的流逝会pop

    def __lt__(self, other):
        return self.end_time < other.end_time

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return self._id


class Solution3:
    """
    优化Solution1, 用id来保存prev和next
    执行用时： 592 ms , 在所有 Python3 提交中击败了 5.47% 的用户
    内存消耗： 64.7 MB , 在所有 Python3 提交中击败了 22.65% 的用户
    """

    def __init__(self, relations, times):
        self.course_dict = self.create_course(times)
        self.init_relations(relations)
        # 每次都要pop最近完成的课程
        self.current_learning = self.init_start_learning_courses()
        self.time = 0

    def get_result(self):
        while self.current_learning:
            first_end_course = heapq.heappop(self.current_learning)
            self.time = first_end_course.end_time
            for next_course_id in first_end_course.next:
                next_course = self.course_dict[next_course_id]
                next_course.prev.remove(first_end_course._id)
                if not next_course.prev:
                    next_course.end_time = self.time + next_course.cost
                    heapq.heappush(
                        self.current_learning,
                        next_course,
                    )
        return self.time

    def create_course(self, times):
        """创建所有课程"""
        course_dict = {
        }
        for index, time in enumerate(times):
            course_dict[index+1] = Course3(
                _id=index+1,
                cost=time,
            )
        return course_dict

    def init_relations(self, relations):
        for pre_id, next_id in relations:
            self.course_dict[pre_id].next.add(
                next_id
            )
            self.course_dict[next_id].prev.add(
                pre_id
            )

    def init_start_learning_courses(self):
        """找到所有没有依赖的课程, 加入current_learning"""
        results = []
        for course in self.course_dict.values():
            if not course.prev:
                course.end_time = course.cost
                results.append(course)
        heapq.heapify(results)
        return results


class Course4:
    """课程对象"""

    def __init__(self, _id, cost: int, end_time=Decimal('inf')):
        """
        cost: 课程需要花费的月份数
        """
        self._id = _id
        self.cost = cost
        self.end_time = end_time  # 默认
        self.prev = []  # 保存的是Courseid, 避免用set每次要hash
        self.next = []  # prev和next随着时间的流逝会pop

    def __lt__(self, other):
        return self.end_time < other.end_time

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return self._id


class Solution4:
    """
    优化Solution1, 用id来保存prev和next
    执行用时： 580 ms , 在所有 Python3 提交中击败了 5.47% 的用户
    内存消耗： 50.7 MB , 在所有 Python3 提交中击败了 25.00% 的用户
    """

    def __init__(self, relations, times):
        self.course_dict = self.create_course(times)
        self.init_relations(relations)
        # 每次都要pop最近完成的课程
        self.current_learning = self.init_start_learning_courses()
        self.time = 0

    def get_result(self):
        while self.current_learning:
            first_end_course = heapq.heappop(self.current_learning)
            self.time = first_end_course.end_time
            for next_course_id in first_end_course.next:
                next_course = self.course_dict[next_course_id]
                next_course.prev.remove(first_end_course._id)
                if not next_course.prev:
                    next_course.end_time = self.time + next_course.cost
                    heapq.heappush(
                        self.current_learning,
                        next_course,
                    )
        return self.time

    def create_course(self, times):
        """创建所有课程"""
        course_dict = {
        }
        for index, time in enumerate(times):
            course_dict[index+1] = Course4(
                _id=index+1,
                cost=time,
            )
        return course_dict

    def init_relations(self, relations):
        for pre_id, next_id in relations:
            self.course_dict[pre_id].next.append(
                next_id
            )
            self.course_dict[next_id].prev.append(
                pre_id
            )

    def init_start_learning_courses(self):
        """找到所有没有依赖的课程, 加入current_learning"""
        results = []
        for course in self.course_dict.values():
            if not course.prev:
                course.end_time = course.cost
                results.append(course)
        heapq.heapify(results)
        return results


class Solution5:
    """
    优化Solution1, 用id来保存prev和next
    执行用时： 696 ms , 在所有 Python3 提交中击败了 5.47% 的用户
    内存消耗： 50.9 MB , 在所有 Python3 提交中击败了 25.00% 的用户
    """

    def __init__(self, relations, times):
        self.time = 0
        self.max_time = 0  # 最小耗时
        self.course_dict = self.create_course(times)
        self.init_relations(relations)
        # 每次都要pop最近完成的课程
        self.current_learning = self.init_start_learning_courses()

    def get_result(self):
        while self.current_learning:
            first_end_course = heapq.heappop(self.current_learning)
            self.time = first_end_course.end_time
            for next_course_id in first_end_course.next:
                next_course = self.course_dict[next_course_id]
                next_course.prev.remove(first_end_course._id)
                if not next_course.prev:
                    next_course.end_time = self.time + next_course.cost
                    heapq.heappush(
                        self.current_learning,
                        next_course,
                    )
        return max(self.time, self.max_time)

    def create_course(self, times):
        """创建所有课程"""
        course_dict = {
        }
        for index, time in enumerate(times):
            course_dict[index+1] = Course4(
                _id=index+1,
                cost=time,
            )
        return course_dict

    def init_relations(self, relations):
        for pre_id, next_id in relations:
            self.course_dict[pre_id].next.append(
                next_id
            )
            self.course_dict[next_id].prev.append(
                pre_id
            )

    def init_start_learning_courses(self):
        """找到所有没有依赖的课程, 加入current_learning"""
        results = []
        for course in self.course_dict.values():
            if not course.prev:
                if not course.next:  # 没有后续的, 不用学了
                    if course.cost >= self.max_time:
                        self.max_time = course.cost
                    continue
                course.end_time = course.cost
                results.append(course)
        heapq.heapify(results)
        return results


class Solution6:
    """
    优化Solution4, 尽可能用 heapreplace 来代替
    heappop和heappush
    """

    def __init__(self, relations, times):
        self.course_dict = self.create_course(times)
        self.init_relations(relations)
        # 每次都要pop最近完成的课程
        self.current_learning = self.init_start_learning_courses()
        self.time = 0

    def get_result(self):
        while self.current_learning:
            first_end_course = self.current_learning[0]
            self.time = first_end_course.end_time
            new_courses = []
            for next_course_id in first_end_course.next:
                next_course = self.course_dict[next_course_id]
                next_course.prev.remove(first_end_course._id)
                if not next_course.prev:
                    next_course.end_time = self.time + next_course.cost
                    new_courses.append(next_course)
            if not new_courses:
                heapq.heappop(self.current_learning)
            else:
                heapq.heapreplace(
                    self.current_learning,
                    new_courses[0])
                for new_course in new_courses[1:]:
                    heapq.heappush(
                        self.current_learning,
                        new_course,
                    )
        return self.time

    def create_course(self, times):
        """创建所有课程"""
        course_dict = {
        }
        for index, time in enumerate(times):
            course_dict[index+1] = Course4(
                _id=index+1,
                cost=time,
            )
        return course_dict

    def init_relations(self, relations):
        for pre_id, next_id in relations:
            self.course_dict[pre_id].next.append(
                next_id
            )
            self.course_dict[next_id].prev.append(
                pre_id
            )

    def init_start_learning_courses(self):
        """找到所有没有依赖的课程, 加入current_learning"""
        results = []
        for course in self.course_dict.values():
            if not course.prev:
                course.end_time = course.cost
                results.append(course)
        heapq.heapify(results)
        return results


class Solution:
    """题目框架"""
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        logging.info(n)
        return Solution6(
            relations=relations,
            times=time,
        ).get_result()


if __name__ == "__main__":
    print(
        Solution().minimumTime(
            n=3,
            relations=[[2, 3]],
            time=[3, 1, 1],
        )
    )
