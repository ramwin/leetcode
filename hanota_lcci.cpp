#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;


class Solution{
  public:
    void hanota(vector<int>& A, vector<int>& B, vector<int>& C) {
      // array<int, A.size()> list;
      for (auto i=A.begin(); i!=A.end(); i++) {
        C.push_back(*i);
      }
      A.clear();
    };
};

int main() {
  vector<int> A = {2, 1, 0};
  vector<int> B = {};
  vector<int> C = {};
  Solution().hanota(A, B, C);
  cout << A.size() << endl;
  cout << C.size() << endl;
};

