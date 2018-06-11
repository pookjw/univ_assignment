//
//  main.cpp
//  calc
//
//  Created by pook on 6/11/18.
//  Copyright © 2018 pook. All rights reserved.
//

#include <iostream>

int convertTwoFromTenNum(int n) {
    int RESULT = 0;
    int a;
    int i;
    for (i = 1; n > 0; i *= 10) {
        a = n % 2; // 2로 나누면 a는 0 또는 1이 나오며, 이는 i가 증감함에 따라 2진수의 자릿수의 숫자로 결정됨
        n /= 2; // 2로 나누면 구하는 2진수의 자릿수가 늘어남
        RESULT += a * i; // 2진수 값 구하는 과정
    }
    return RESULT;
}

int main(int argc, const char * argv[]) {
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int c = convertTwoFromTenNum(a);
    if (b != 1){
        for (int i=1; i<b; i++){
            c /= 10;
        }
    }
    printf("%d\n", c%2);
    return 0;
}
