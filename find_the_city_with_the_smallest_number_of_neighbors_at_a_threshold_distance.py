#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-04-04 08:48:15


class Node(int):

    def __init__(self, index):
        self.index = index
        self.neighbours = {}

    def get_node_with_distance(self, distance, exclude_node_set=set()):
        
        for neighbour, distance in self.neighbours.items():

    def get_all_node_with_distance(self, distance):



class Solution:


    def findTheCity(self, n, edges, distanceThreshold):
        self.node_dict = {}
        for i in range(n):
            self.node_dict[i] = Node(i)
        for edge in edges:
            self.node_dict[edge[0]].neighbours[
                self.node_dict[edge[1]]
            ] = edge[2]
            self.node_dict[edge[1]].neighbours[
                self.node_dict[edge[0]]
            ] = edge[2]


solution = Solution()
solution.findTheCity(
    4,
    [[0,1,3],[1,2,1],[1,3,4],[2,3,1]],
    4
)
