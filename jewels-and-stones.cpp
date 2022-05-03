#include <stdio.h>
#include <iostream>

// 执行用时： 0 ms , 在所有 C++ 提交中击败了 100.00% 的用户
// 内存消耗： 6 MB , 在所有 C++ 提交中击败了 87.69% 的用户

using namespace std;

class Solution {
  public:
    int numJewelsInStones(string jewels, string stones) {
      int number=0;
      for (auto i=stones.begin(); i!=stones.end(); i++) {
        if (jewels.find(*i) != jewels.npos) {
          cout << jewels.find(*i) << endl;
          number ++;
        }
      }
      return number;
    }
};


int main() {
  cout << Solution().numJewelsInStones(
    "aA",
    "aAAbbbb"
  );
  return 0;
};

