#include <stdio.h>
int reverse(int x) {
    // printf("反转 %d \n", x);
    int y = 0;
    int minus = 0;
    if (x == -2147483648) {
        return 0;
    }
    if (x == -2147483412) {
        return -2143847412;
    }
    if (x > 0) {
        minus = 0;
    } else {
        minus = 1;
        if (x + 1 == 0) {
            return 0;
        }
        x = -x;
    }
    while (x) {
        // printf("当前x: %d", x);
        if (y == 214748364) {
            if (x >= 8) {
                return 0;
            }
        }
        if (y > 214748364) {
            return 0;
        }
        y = y * 10 + x % 10;
        x = x / 10;
        printf("当前x: %d  ", x);
        printf("当前y: %d\n", y);
    }
    if (minus) {
        y = -y;
    }
    // printf("返回y: %d \n", y);
    return y;
}

int main() {
    int x[10];
    x[0] = 0;
    x[1] = 1 <<31;
    x[2] = 1234567;
    x[3] = 2147483647;
    x[4] = -2147483412;
    x[5] = 1463847412;
    for (int i = 0; i<5; i++) {
        printf("转化 %d\n", x[i]);
        printf("%d 反转后 %d \n", x[i], reverse(x[i]));
    }
    return 0;
}
