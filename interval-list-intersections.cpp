#include <stdio.h>
#include <iostream>
#include <vector>

#define LOG true
using namespace std;



class ListStatus {
  public:
    bool in=false;  // 是否在里面
    int next=0;  // 下一个数字
    int index=0;  // out的时候, index+1 当前处于第几个列表
    vector<vector<int>> &list;
    ListStatus(vector<vector<int>> &list): list(list) {
      next=list[0][0];
    };
};

class Solution2 {
  public:
    ListStatus first_status;
    ListStatus second_status;
    int number=0;
    int both_left=-1;  // 记录之前遇到的共同的左区间
    vector<vector<int>> result;
    Solution2(ListStatus first_status, ListStatus second_status): first_status(first_status), second_status(second_status) {
    }
    vector<vector<int>> intervalIntersection() {
      number = -1;
      while (first_status.index != first_status.list.size() && second_status.index != second_status.list.size()) {
        move();
      }
      if (both_left >= 0) {
        if (first_status.in and !second_status.in) {
          vector<int> both = {both_left, second_status.next};
          result.push_back(both);
        } else if (!first_status.in and second_status.in) {
          vector<int> both = {both_left, first_status.next};
          result.push_back(both);
        }
      }
      return result;
    };
  private:
    void move() {
      if (LOG) cout << "当前数字: " << number << endl;
      // 数字往前走
      if (first_status.next == second_status.next) {
        if (LOG) cout << "数字一样大\n";
        number = second_status.next;
        if (first_status.in && second_status.in) {
          vector<int> both = {both_left, number};
          result.push_back(both);
          both_left = -1;
        } else {
          both_left = number;
        }
        pivote(first_status);
        pivote(second_status);
        if ((first_status.in && !second_status.in) || (!first_status.in && second_status.in)) {
          both_left = -1;
          result.push_back(vector<int> {number, number});
        };
      } else { 
        ListStatus* meet;
        ListStatus* unmeet;
        if (first_status.next < second_status.next) {
          meet = &first_status;
          unmeet = &second_status;
        } else {
          unmeet = &first_status;
          meet = &second_status;
        }
        if (LOG) cout << "number从" << number << "变成" << meet->next << endl;
        number = meet->next;
        if (meet->in and unmeet->in) {
          if (LOG) cout << "都进入， 现在退出" << endl;
          vector<int> both = {both_left, meet->next};
          result.push_back(both);
          both_left = -1;
        };
        pivote(*meet);
        if (meet->in and unmeet->in) {
          // cout << "进入了" << endl;
          both_left=number;
        };
      }
      // cout << "遇到了数字: " << number << endl;
    }
    void pivote(ListStatus & status) {
      // 数字碰到了某个status
      if (LOG) cout << "数组遇到了";
      if (status.in) {
        status.index++;
        if (status.index != status.list.size()) {
          status.next = status.list[status.index][0];
        }
      } else {
        status.next = status.list[status.index][1];
      }
      status.in = !status.in;
      if (LOG)  cout << "in变成: " << status.in;
      if (LOG)  cout << "next变成了: " << status.next;
      if (LOG)  cout << "index变成了: " << status.index;
      if (LOG)  cout << endl;
    }
};


class Solution {
  public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
      if (firstList.size() == 0 || secondList.size() == 0) {
        vector<vector<int>> result;
        return result;
      };
      return Solution2(
          ListStatus(firstList),
          ListStatus(secondList)
      ).intervalIntersection();
    };
};

void print(vector<int> & list) {
  for (auto i=list.begin(); i!=list.end();i++) {
    cout << *i << ',';
  }
  cout << endl;
};


void print(vector<vector<int>> & list) {
  for (auto i=list.begin(); i!=list.end(); i++) {
    print(*i);
  }
};

int main() {
  vector<vector<int>> firstList = {
    vector<int> {1, 7},
  };
  vector<vector<int>> secondList = {
    vector<int> {3, 10},
  };
  vector<vector<int>> result = Solution().intervalIntersection(firstList, secondList);
  print(result);
};
