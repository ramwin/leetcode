#include <stdio.h>
#include <iostream>

using namespace std;


class Solution {
  public:
    bool isPalindrome(int x) {
      string str = to_string(x);
      for (int i=0; i <= str.size() / 2; i++) {
        if (str[i] != str[str.size()-i-1]) {
          return false;
        }
      }
      return true;
    };
};

int main() {
  cout << Solution().isPalindrome(121) << endl;
};

