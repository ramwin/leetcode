#include <stdio.h>
#include <iostream>
#include <map>

using namespace std;


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
      if (s.size() == 1) {
        return 1;
      }
      int max_length = 0;
      int start = 0;
      int previous_index = 0;
      char current;
      // cout << "start" << start;
      map<char, unsigned int> last_seen_position;
      for (int index=0; index<s.size(); index++) {
        current = s[index];
        // cout << "查看字母" << current << endl;
        if (last_seen_position.find(current) == last_seen_position.end()) {
          previous_index = -1;
        } else {
          previous_index = last_seen_position[current];
        }
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

