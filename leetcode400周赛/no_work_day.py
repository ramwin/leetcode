#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        return days - sum((
                meeting[1] - meeting[0] + 1
                for meeting in self.get_range(meetings)
                ))

    def get_range(self, meetings: List[List[int]]):
        """返回去重以后的会议"""
        meetings.sort(key=lambda x: x[0])
        print(meetings)
        new_meetings = []
        previous_meeting = None
        for meeting in meetings:
            if previous_meeting is None:
                new_meetings.append(meeting)
                previous_meeting = meeting
            else:
                if meeting[1] <= previous_meeting[1]:
                    continue
                # 新的会议只考虑后面的时间
                previous_meeting = (
                        max(meeting[0], previous_meeting[1] + 1),
                        meeting[1]
                        )
                new_meetings.append(previous_meeting)
        return new_meetings
