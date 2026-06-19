// 超过了100%的人
#include <stdio.h>
#include <iostream>
#include <map>

using namespace std;

int last_seen_position[256];


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
      for (int i=0; i<256; i++) {
        last_seen_position[i] = -1;
      };
      if (s.size() == 1) {
        return 1;
      }
      int max_length = 0;
      int start = 0;
      int previous_index;
      char current;
      // cout << "start" << start;
      //
      for (int index=0; index<s.size(); index++) {
        current = s[index];
        // cout << "查看字母" << current << endl;
        // auto find = last_seen_position.find(current);
        // find = last_seen_position.find(current);
        // cout << find -> first << endl;
        // if (find == last_seen_position.end()) {
        //   previous_index = -1;
        // } else {
        //   previous_index = find -> second;
        // }
        previous_index = last_seen_position[current];
        last_seen_position[current] = index;
        if (previous_index >= start) {
          start = previous_index + 1;
        };
        int length = (index - start + 1);
        if (length > max_length) {
          max_length = length;
        }
      };
      return max_length;
    }
};

int main() {
  Solution a;
  cout << a.lengthOfLongestSubstring("ababcdadecba") << endl;
  cout << a.lengthOfLongestSubstring(" ") << endl;
  cout << a.lengthOfLongestSubstring("aua") << endl;
  cout << a.lengthOfLongestSubstring("aub") << endl;
};

