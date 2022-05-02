// 执行用时： 8 ms , 在所有 C++ 提交中击败了 95.76% 的用户
// 内存消耗： 17.1 MB , 在所有 C++ 提交中击败了 29.48% 的用户

#include <stdio.h>
// #include <iostream>
#include <map>
#include <vector>
// #include <algorithm>

using namespace std;

int same(int max, int min) {
  // 最大公约数
  if (max%min == 0) {
    return min;
  }
  if (max < min) {
    return same(min, max);
  }
  return same(min, max % min);
};

class Solution {
  public:
    bool hasGroupsSizeX(vector<int>& deck) {
      map<int, int> int_counter;
      for (auto i=deck.begin(); i!=deck.end(); i++) {
        int_counter[*i]++;
      };
      // print(int_counter);
      std::vector<int> heap;
      int minimum = 0;
      for (const auto& [key, value]: int_counter) {
        if (minimum == 0) minimum = value;
        if (value < minimum) { minimum = value; }
        heap.push_back(value);
      };
      for (const auto& [key, value]: int_counter) {
        minimum = same(value, minimum);
        if (minimum == 1) return false;
      };
      return true;
      // make_heap(heap.begin(), heap.end());
      // int max = 0;
      // if (minimum == 1) {
      //   return false;
      // };
      // while (heap.size()) {
      //   // cout << "处理前" << "当前min: " << minimum << endl;
      //   // print(heap);
      //   max = heap.front();
      //   pop_heap(heap.begin(), heap.end());
      //   heap.pop_back();
      //   // cout << "max:" << max << endl;
      //   minimum = same(max, minimum);
      //   if (minimum == 1) return false;
      //   make_heap(heap.begin(), heap.end());
      //   // cout << "处理后" << "当前min: " << minimum << endl;
      //   // print(heap);
      // }
      // return true;
    };
};

int main() {
  vector<int> deck1 = {1,2,3,4,4,3,2,1};
  // if (Solution().hasGroupsSizeX(deck1) != 1) cout << "错误";
  vector<int> deck2 = {1, 1, 1, 1, 1, 0, 0, 0};
  // if (Solution().hasGroupsSizeX(deck2) != 0) cout << "错误";
  vector<int> deck3 = {1, 1};
  // if (Solution().hasGroupsSizeX(deck3) != 1) cout << "错误";
  return 0;
};
