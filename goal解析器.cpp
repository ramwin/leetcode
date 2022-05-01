#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;


enum Status {
  normal,
  first_bracket,
  in_bracket
};


class Solution1 {
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

class Solution2 {
  public:
    string interpret(string command) {
      char result[command.size()+1];
      int index = 0;
      Status status;
      for (auto i = command.begin(); i != command.end(); i++) {
        if (*i == 'G') {
          result[index] = 'G';
          index++;
          continue;
        } else if (*i == '(') {
          status = first_bracket;
          continue;
        } else if (*i == ')') {
          if (status == in_bracket) {
            result[index] = 'a';
            result[index+1] = 'l';
            index+=2;
          } else if (status == first_bracket) {
            result[index] = 'o';
            index++;
          }
          status = normal;
          continue;
        } else if (*i == 'a') {
          status = in_bracket;
          continue;
        }
      }
      result[index] = '\0';
      string result2;
      result2 = result;
      return result2;
    }
};

int main() {
  string input = "G()(al)";
  string output = Solution2().interpret(input);
  cout << output << endl;
};
