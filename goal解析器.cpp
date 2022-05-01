#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;


enum Status {
  normal,
  first_bracket,
  in_bracket
};


class Solution {
  public:
    string interpret(string command) {
      string result;
      Status status;
      for (auto i = command.begin(); i != command.end(); i++) {
        if (*i == 'G') {
          result += 'G';
          continue;
        } else if (*i == '(') {
          status = first_bracket;
          continue;
        } else if (*i == ')') {
          if (status == in_bracket) {
            result += "al";
          } else if (status == first_bracket) {
            result += 'o';
          }
          status = normal;
          continue;
        } else if (*i == 'a') {
          status = in_bracket;
          continue;
        }
      }
      return result;
    }
};

int main() {
  string input = "G()()()(al)";
  string output = Solution().interpret(input);
  cout << output << endl;
};
