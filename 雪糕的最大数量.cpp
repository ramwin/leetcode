// 8ms击败93.11%
// 78.82MiB 击败19.67%
#include <stdio.h>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

#define size 100001
int cost_cnt[size + 1];

class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
      memset(cost_cnt, 0, sizeof(cost_cnt));
      for (int i: costs) {
        cost_cnt[i]++;
      };
      int total_money;
      int bought_cnt = 0;
      for (int j=1; j<=size; j++) {
        total_money = cost_cnt[j] * j;
        if (coins > total_money) {
          coins -= total_money;
          bought_cnt += cost_cnt[j];
        } else {
          bought_cnt += coins / j;
          break;
        }
      };
      return bought_cnt;
    }
};

int main() {
  Solution a;
  // vector<int> costs = {1, 3, 2, 4, 1};
  // cout << a.maxIceCream(costs, 7) << "== 7\n";
  // vector<int> costs = {1,6,3,1,2,5};
  // cout << a.maxIceCream(costs, 20) << "== 6\n";
  vector<int> costs = {10, 6, 8, 7, 7, 8};
  cout << a.maxIceCream(costs, 5) << "== 0\n";
};

