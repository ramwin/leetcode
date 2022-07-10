#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


// 执行用时： 4 ms , 在所有 C++ 提交中击败了 86.79% 的用户
// 内存消耗： 9.7 MB , 在所有 C++ 提交中击败了 81.06% 的用户


class Solution {
  public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
      std::sort(nums1.begin(), nums1.end());
      std::sort(nums2.begin(), nums2.end());
      int index1 = 0;
      int index2 = 0;
      vector<int> result;
      while (index1 < nums1.size() && index2 < nums2.size()) {
        if (nums1[index1] < nums2[index2]) {
          index1++;
        } else if (nums1[index1] > nums2[index2]) {
          index2++;
        } else {
          result.push_back(nums1[index1++]);
          index2++;
        }
      };
      return result;
    }
};
