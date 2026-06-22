// 执行用时击败100%, 消耗内存8.75MiB, 击败59.5%
#include <stdio.h>
#include <iostream>
#include <map>

using namespace std;



class Solution {
public:
    int maxNumberOfBalloons(string text) {
      int count[255];
    //   cout << text << endl;
      for (char i: text) {
        // cout << i << endl;
        if (i == 'b' || i == 'a' || i == 'l' || i == 'o' || i == 'n') {
          count[i]++;
        }
      };
      unsigned int result = 10000;
      if (count['b'] < result) {
        result = count['b'];
      }
      if (count['a'] < result) {
        result = count['a'];
      }
      if (count['n'] < result) {
        result = count['n'];
      }
      if (count['l'] / 2 < result) {
        result = count['l'] / 2;
      }
      if (count['o'] / 2 < result) {
        result = count['o'] / 2;
      }
      return result;
    }
};


int main() {
  Solution a;
  // cout << a.maxNumberOfBalloons("loonbalxballpoon") << endl;
  cout << a.maxNumberOfBalloons("nlaebolko") << endl;
};

