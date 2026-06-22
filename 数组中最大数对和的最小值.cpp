//
// 75ms击败43.46%, 97.82MiB击败36.29%

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int minPairSum(vector<int>& nums) {
      sort(nums.begin(), nums.end());
      int result = 0;
      int tmp;
      for (int j=0; j<nums.size()/2; j++) {  // 循环次数太多,考虑到题目的n<10**5, nums[i] <10**5, 应该用桶遍历.
        cout << j << endl;
        tmp = nums[j] + nums[nums.size() - j - 1];
        cout << tmp << endl;
        if (tmp > result) {
          result = tmp;
        }
        cout << endl;
      };
      return result;
    }
};

int main() {
  Solution a;
  // vector<int> nums = {4,1,5,1,2,5,1,5,5,4};
  vector<int> nums = {3, 5, 2, 3};
  cout << a.minPairSum(nums) << endl;
};

