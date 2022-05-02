// 执行用时： 132 ms , 在所有 C++ 提交中击败了 38.12% 的用户
// 内存消耗： 70 MB , 在所有 C++ 提交中击败了 95.84% 的用户

#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
  public:
    int longestUnivaluePath(TreeNode* root) {
      if (root == nullptr) {return 0;};
      int _max = max(
          longestUnivaluePath(root->left),
          longestUnivaluePath(root->right)
      );
      _max = max(
        _max,
        longestUnivaluePath(root->left, root->val) +
        longestUnivaluePath(root->right, root->val)
      );
      return _max;
    };
    int longestUnivaluePath(TreeNode* & root, int & require) {
      // 返回至多几个经过根节点的节点数字都是require
      if (root == nullptr) {return 0;};
      if (root->val != require) {return 0;};
      return max(
        longestUnivaluePath(root->left, require),
        longestUnivaluePath(root->right, require)
      ) + 1;
    };
};


int main() {
  TreeNode node_3_3(5);
  TreeNode node_2_2(5, &node_3_3, nullptr);
  TreeNode node_1_1(5, nullptr, &node_2_2);
  cout << Solution().longestUnivaluePath(&node_1_1) << endl;
};
