// 超时了,当n很大时,需要像汉诺塔或者斐波拉契数列一样用举证的指数计算
#include <stdio.h>
#include <iostream>
#include <map>

#define DEBUG true

using namespace std;

enum Direction {
  TO_LEFT,
  TO_RIGHT,
};


struct Key {
  Direction direction;
  long start;  // 相对0来说的.
  long end;  // 包含end;
  long n;  // 跳动几次
  bool operator<(const Key& other) const {
    if (direction != other.direction) return direction < other.direction;
    if (start != other.start) return start < other.start;
    if (end != other.end) return end < other.end;
    return n < other.n;
  }
};


map<struct Key, long> caches;  // 保存从start开始往Direction来回移动n步的数字

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
      r = r - l;
      l = 0;
      int result = 0;
      int tmp = 0;
      for (int i=0; i<=r; i++) {
#if DEBUG
        cout << "level1: 从" << i << "开始" << endl;
#endif
        for (auto direction: {TO_LEFT, TO_RIGHT}) {
#if DEBUG
          cout << "方向" << direction << endl;
#endif
          tmp = zigZagArrays_withDirection({
              direction,
              i,
              r,
              n-1,
          });
          result = (tmp + result) % (1000000007);
#if DEBUG
          cout << "次数" << tmp << endl;
#endif
        };
      };
      return result;
    };
      // 动态规划,看减少n还是减少r
      // 把锯齿形状分为先凸形和先凹形;
      // n, l, r分两种
      // n-1, l, r 后面的lr是凹形, 凹形就是(l, l+1..., r-1, r)每种加凸性(但是第一个元素小于l, l+1..., r-1, r)
      // n-1, l, r 后面的lr是凸形
      //
      // 第二种方案减少l(l选不选
      // 不选
      // f(n, l, r)1 = f(n - 1, l+1, r)
      // 选(放第一个还是非第一个). 因为l最小, 所以是l+1...r分成2个前凸+后凸
      // f(n, l, r)2 =

      // 不对, 理论上来说<n, l, r>等价于<n, 0, r-l>
      // <n, l, r>看第一个元素是x, 后面就是<n, x+1, r> ... class Solution {
    int zigZagArrays_withDirection(struct Key key) {
      int tmp;
      if (key.n == 1) {
        if (key.direction == TO_LEFT) {
          if (key.start == 0) {
            return 0;
          };
          return key.start;
        } else {
          // n=2是,从0开始有 01, 02
          return key.end - key.start;
        }
      }
      if (caches.find(key) == caches.end()) {
        int result = 0;
        // 从start开始有2个方向, 先往左, 后往右走n-1步
        struct Key newkey;
        newkey.n = key.n - 1;
        newkey.end = key.end;
        if (key.direction == TO_LEFT) {
          newkey.direction = TO_RIGHT;
          for (int i=0; i<key.start; i++) {
            newkey.start = i;
            tmp = zigZagArrays_withDirection(newkey);
            result = (tmp + result) % (1000000007);
#if DEBUG
            printf("  start为%d的往右的次数有%d\n", i, tmp);
#endif
          };
        } else {
        // 先往右
          newkey.direction = TO_LEFT;
          for (int i=key.start + 1; i<=key.end; i++) {
            newkey.start = i;
            tmp = zigZagArrays_withDirection(newkey);
#if DEBUG
            printf("  start为%d的往左的次数有%d\n", i, tmp);
#endif
            result = (tmp + result) % (1000000007);
          };
        }
        caches[key] = result;
      };
      return caches[key];
    }
};

int main() {
  Solution solution;
  /*
  cout << solution.zigZagArrays(2, 0, 1) << endl;
  cout << solution.zigZagArrays_withDirection({
      TO_RIGHT,
      0,
      1,
      1,
  }) << endl;
  */
  cout << solution.zigZagArrays_withDirection({
      TO_RIGHT,
      // 0,  // 从0开始
      // 2,  // 021, 010, 020
      //
      1,  // 从1开始
      2,  // 121, 120
      2,
  }) << endl;;
  cout << "测试022应该等于3" << endl;
  cout << solution.zigZagArrays_withDirection({
      TO_RIGHT,
      0,  // 从0开始
      2,  // 021, 010, 020
      2,
  }) << endl;;
  cout << endl;
  // 010 020 021
  cout << "测试3, 0, 2" << endl;
  cout << solution.zigZagArrays(3, 0, 2) << endl;

  cout << "测试从3开始动2个应该等于3" <<endl;
  cout << solution.zigZagArrays_withDirection({
      TO_LEFT,
      2,  // start = 2
      2,  // 最大是2
      2,  // 走2步, 212, 202, 201
  }) << endl;

  cout << endl;

  cout << "aaa应该等于2" << endl;
  cout << solution.zigZagArrays_withDirection({
      TO_RIGHT,
      0,  // start = 0
      2,  // 最大是2
      1,  // 走1步, 01, 02
  }) << endl;
  cout << endl;

  cout << "应该等于1" << endl;
  cout << solution.zigZagArrays_withDirection({
      TO_LEFT,
      1,  // 从1开始
      2,  // 10
      1,
  }) << endl;;
  //
  cout << endl;

  cout << "应该等于2" << endl;
  cout << solution.zigZagArrays(3, 0, 1) << endl;
  cout << endl;

  cout << "应该等于1" << endl;
  cout << solution.zigZagArrays_withDirection({
      TO_RIGHT,
      0,  // 从0开始
      1,  // 01
      1,
  }) << endl;
  cout << endl;
  return 0;
};
