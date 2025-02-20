#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;


class Solution {
  public:
    int getDivScore(vector<int>& num, vector<int>& divisors) {
      int result = 0;
      for (int i: divisors) {
        if (num % i == 0) {
          result++;
        }
      };
      return result;
    };
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
      int result = 0;
      int max;
      for (int num: nums) {
        max = getDivScore(num, divisors);
        if (max > result) {
          result = max;
        }
      }
      return max;
    };
};


int main() {
  vector<int> a = {4, 7, 9, 3, 9};
  vector<int> b = {5, 2, 3};
  cout << Solution().maxDivScore(
      a, b
  );
};

