#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-03-02 22:41:20


"""
i   i     i      i     i
i   i    i    a  i   i
car_fleet = 起点 [left_car_fleet ] [ slow] [right_car_fleet] 终点

[10, 8, 0, 5, 3]
[2, 4, 1, 1, 3]
[(0, 1), (3, 3), (5, 1), (8, 4), (10, 2)]

[0, 3, 5, 8, 10]  12
[1, 3, 1, 4, 2]

"""

class Solution:

    def carFleet(self, target, positions, speeds):
        """position: 数字越大离终点越近"""
        new_positions = []
        new_speeds = []
        for position, speed in sorted(zip(positions, speeds)):
            new_positions.append(position)
            new_speeds.append(speed)
        return self.get_car_fleet(target, new_positions, new_speeds)

    def in_one_fleet(self,
                     left_position, left_speed,
                     right_position, right_speed, 
                     target):
        """校验两个车是否在同一个fleet"""
        if left_position >= target:
            return True
        if right_position >= target:
            return False
        return (target-left_position)*(right_speed) <= (target-right_position)*(left_speed)
            
    def get_car_fleet(self, target, positions, speeds):
        slowest_speed = min(speeds)
        slowest_index = speeds.index(slowest_speed)
        length = len(speeds)
        if length == 1:
            return 1
        if length == 0:
            return 0
        total = 0
        if slowest_index == 0:
            if self.in_one_fleet(
                positions[slowest_index], speeds[slowest_index],
                positions[slowest_index+1], speeds[slowest_index+1],
                target,
            ):
                return self.get_car_fleet(
                    target, positions[1:], speeds[1:]
                )
            else:
                return 1 + self.get_car_fleet(
                    target, positions[1:], speeds[1:]
                )

        if slowest_index +1 == len(positions):
            if self.in_one_fleet(
                positions[slowest_index-1], speeds[slowest_index-1],
                positions[slowest_index], speeds[slowest_index],
                target,
            ):
                return self.get_car_fleet(
                    target, positions[:slowest_index], speeds[:slowest_index]
                )
            else:
                return 1 + self.get_car_fleet(
                    target, positions[:slowest_index], speeds[:slowest_index]
                )

        total = self.get_car_fleet(
            target, positions[:slowest_index], speeds[:slowest_index]
        ) + 1 + self.get_car_fleet(
            target, positions[slowest_index:], speeds[slowest_index:]
        )
        if self.in_one_fleet(
            positions[slowest_index-1], speeds[slowest_index-1],
            positions[slowest_index], speeds[slowest_index],
            target,
            ):
            total = total - 1
        if self.in_one_fleet(
            positions[slowest_index], speeds[slowest_index],
            positions[slowest_index+1], speeds[slowest_index+1],
            target,
            ):
            total = total - 1
        return total


"""
以最后一个到终点的车来分割这个车队
car_fleet = 起点 [left_car_fleet ] [ latest] [right_car_fleet] 终点
"""


class Solution:
    def carFleet(self, target, position, speed):
        new_positions = []
        new_speeds = []
        new_times = []  # 代表了每一辆车到达终点的时间
        positions = position
        speeds = speed
        for position, speed in sorted(zip(positions, speeds)):
            new_positions.append(position)
            new_speeds.append(speed)
            new_times.append((target-position)/speed)
        
        return self.get_car_fleet(target, new_positions, new_speeds, new_times)

    def get_car_fleet(self, target, positions, speeds, times):
        length = len(speeds)
        if length == 1:
            return 1
        if length == 0:
            return 0
        # print("get_car_fleet")
        # print("positions:", end=" ")
        # print(positions)
        # print("speeds:", end=" ")
        # print(speeds)
        # print("times:", end=" ")
        # print(times)
        latest_time = max(times)
        latest_index = times.index(latest_time)
        if latest_index + 1 == length:
            return 1
        total = 0
        right_car_fleet_cnt = self.get_car_fleet(target, positions[latest_index+1:], speeds[latest_index+1:], times[latest_index+1:])
        if max(times[latest_index+1:]) >= times[latest_index]:
            return right_car_fleet_cnt
        else:
            return right_car_fleet_cnt + 1

solution = Solution()
target, position, speed = (
    12,
    [10,8,0,5,3],
    [2,4,1,1,3]
)

print(solution.carFleet(target, position, speed))
assert solution.carFleet(target, position, speed) == 3


target, position, speed = (
    10,
    [],
    []
)

assert solution.carFleet(target, position, speed) == 0


target, position, speed = (
    10,
    [2, 4],
    [3, 2]
)

assert solution.carFleet(target, position, speed) == 1