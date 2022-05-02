#include <stdio.h>
#include <iostream>
#include <vector>

// 执行用时： 0 ms , 在所有 C++ 提交中击败了 100.00% 的用户
// 内存消耗： 9.1 MB , 在所有 C++ 提交中击败了 93.20% 的用户

using namespace std;

class Solution{
  public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
      // 当作一棵树来查找 O(m+n)
      int row = 0;
      int column = 0;
      if (matrix.size() == 0) { return false; };
      if (matrix[0].size() == 0) { return false; };
      return searchMatrix(matrix, target, row, column);
    };
    bool searchMatrix(vector<vector<int>>& matrix, int& target, int& row, int& column) {
      // 当作数来查找 O(m+n)
      if (column == matrix[0].size()) {return false;};  // 走头无路了
      if (matrix[row][column] == target) {return true;};
      if (matrix[row][column] > target) {return false;};
      if (row != matrix.size() - 1 && matrix[row+1][column]<=target) {
        row++;
        return searchMatrix(matrix, target, row, column);
      }
      column++;
      return searchMatrix(matrix, target, row, column);
    };
};


int main() {
};

