#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;



class ListStatus {
  public:
    bool in;  // 是否在里面
    int next;  // 下一个数字
    int index;  // out的时候, index+1 当前处于第几个列表
    vector<vector<int>> &list;
    ListStatus(vector<vector<int>> &list): list(list) {
    };
};

class Solution2 {
  public:
    ListStatus first_status;
    ListStatus second_status;
    int number;
    int both_left;  // 记录之前遇到的共同的左区间
    vector<vector<int>> result;
    Solution2(ListStatus first_status, ListStatus second_status): first_status(first_status), second_status(second_status) {
    }
    vector<vector<int>> intervalIntersection() {
      if (first_status.list.size() == 0 || second_status.list.size() == 0) {
        return result;
      };
      number = -1;
      while (first_status.index != first_status.list.size() && second_status.index != second_status.list.size()) {
        move();
      }
      if (first_status.in and !second_status.in) {
        vector<int> both = {both_left, second_status.next};
        result.push_back(both);
      } else if (!first_status.in and second_status.in) {
        vector<int> both = {both_left, first_status.next};
        result.push_back(both);
      }
      return result;
    };
  private:
    void move() {
      // 数字往前走
      if (first_status.next == second_status.next) {
        number = second_status.next;
        if (first_status.in && second_status.in) {
          vector<int> both = {both_left, number};
          result.push_back(both);
          both_left = 0;
        } else {
          both_left = number;
        }
        pivote(first_status);
        pivote(second_status);
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
        if (meet->in and unmeet->in) {
          vector<int> both = {both_left, meet->next};
          result.push_back(both);
        } else {
          pivote(*meet);
        };
      }
    }
    void pivote(ListStatus & status) {
      // 数字碰到了某个status
      if (status.in) {
        status.index++;
        if (status.index != status.list.size()) {
          status.next = status.list[status.index][0];
        }
      } else {
        status.next = status.list[status.index][1];
      }
      status.in = !status.in;
    }
};


class Solution {
  public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
      return Solution2(
          ListStatus(firstList),
          ListStatus(secondList)
      ).intervalIntersection();
    };
};


int main() {
};

