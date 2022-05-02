#include <stdio.h>
#include <iostream>


using namespace std;


struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};



// 执行用时： 28 ms , 在所有 C++ 提交中击败了 92.79% 的用户
// 内存消耗： 32.7 MB , 在所有 C++ 提交中击败了 24.11% 的用户
class Solution1 {
  public:
    TreeNode* convertBST(TreeNode* root) {
      if (root == nullptr) {
        return nullptr;
      };
      return convertBST(root, 0);
    };
    TreeNode* convertBST(TreeNode* root, int add) {
      if (root->right != nullptr) {
        convertBST(root->right, add);
        root->val += get_sum(root->right);
      } else {
        root->val += add;
      }
      if (root->left != nullptr) {
        convertBST(root->left, root->val);
      }
      return root;
    };
  private:
    int get_sum(TreeNode* root) {
      if (root->left == nullptr) {
        return root->val;
      };
      return get_sum(root->left);
    }
};



// 执行用时： 28 ms , 在所有 C++ 提交中击败了 92.79% 的用户
// 内存消耗： 32.6 MB , 在所有 C++ 提交中击败了 79.04% 的用户
class Solution {
  public:
    TreeNode* convertBST(TreeNode* root) {
      if (root == nullptr) {
        return nullptr;
      };
      convertBST(root, 0);
      return root;
    };
    int convertBST(TreeNode* root, int add) {
      // 转化后，直接返回int, 避免二次获取get_sum
      if (root->right != nullptr) {
        root->val += convertBST(root->right, add);
      } else {
        root->val += add;
      }
      if (root->left != nullptr) {
        return convertBST(root->left, root->val);
      };
      return root->val;
    };
};

int main() {
};
