// https://leetcode.cn/problems/find-the-highest-altitude/?envType=daily-question&envId=2026-06-19

#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;


class Solution {
  public:
    int largestAltitude(vector<int>& gain) {
      int highest = 0;
      int latitude = 0;
      for (auto i: gain) {
        latitude += i;
        if (latitude > highest) {
          highest = latitude;
        };
      };
      return highest;
    }
};

int main() {
  Solution a;
  vector<int> b{-5, 1, 5, 0, -7};
  cout << a.largestAltitude(b);
};
