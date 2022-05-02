#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;


class Solution {
  public:
    string toLowerCase(string s) {
      char result[s.size() + 1];  // 多留一个\0用来告诉string,这个地方结束了
      for (int i=0; i<s.size(); i++) {
        result[i] = tolower(s[i]);
      };
      result[s.size()] = '\0';
      return result;
    };
};

int main() {
  string s = "Hello";
  string r = Solution().toLowerCase(s);
  cout << r << endl;
};
