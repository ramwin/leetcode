#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;


class Solution {
  public:
    vector<int> twoSum(vector<int>& nums, int target) {
      vector<int> sorted = nums;
      sort(sorted.begin(), sorted.end());
      int begin = 0;
      int end = sorted.size() - 1;
      while (end > begin) {
        int result = sorted[end] + sorted[begin];
        // cout << sorted[begin] << "+" << sorted[end] << "=" << result << endl;
        if (result == target) {
          break;
        } else if (result > target) {
          end --;
        } else {
          begin++;
        }
      }
      cout << "数字1: " << sorted[begin] << endl;
      cout << "数字2: " << sorted[end] << endl;
      int number1_index = -1;
      int number2_index = -1;
      int another_find;
      int index = 0;
      for (int i=0; i<nums.size(); i++) {
        if (nums[i] == sorted[begin]) {
          index = i;
          number1_index=i;
          another_find = sorted[end];
          break;
        } else if (nums[i] == sorted[end]) {
          index = i;
          number1_index=i;
          another_find = sorted[begin];
          break;
        }
      }
      for (int i=index; i<nums.size(); i++) {
        if (nums[i] == another_find) {
          number2_index = i;
        };
      }
      return {number1_index, number2_index};
    };
};

int main() {
  // vector<int> nums = {3,2,4};
  // int target = 6;
  // vector<int> result =Solution().twoSum(nums, target);
  // cout << result[0] << endl;
  // cout << result[1] << endl;

  // vector<int> nums = {3, 3,};
  // int target = 6;
  // vector<int> result =Solution().twoSum(nums, target);
  // cout << result[0] << endl;
  // cout << result[1] << endl;
  vector<int> nums = {-1, -2, -3, -4, -5};
  int target = -8;
  vector<int> result =Solution().twoSum(nums, target);
  cout << result[0] << endl;
  cout << result[1] << endl;
};
