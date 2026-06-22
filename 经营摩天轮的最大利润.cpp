#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int current_profit = 0;
    int _runningCost = 0;
    int minOperationsMaxProfit(vector<int>& customers, int boardingCost, int runningCost) {
      short chairs[4] = {0};  // 每个椅子上当前有多少人;
      int waiting = 0;  // 当前多少人在等待;
      int result = 0;  // 最多获取多少利润;
      _runningCost = runningCost;
      while (true) {  // 应该根据乘客循环;
        rotate();
        if (current_profit >= result) {
          result = current_profit;
        };
      };
      return result;
    };
private:
    void rotate() {
      // TODO 旋转.每个座舱后面的人挪到前面去, 收取一定费用. 
      current_profit -= _runningCost;
      cout << "当前利润" << current_profit;
      // 最后一个座舱坐N(最多4)个人并收费;
    };
};


int main() {
  Solution a;
  vector<int> customers = {1, 2, 3};
  a.minOperationsMaxProfit(customers, 1, 1);
};
