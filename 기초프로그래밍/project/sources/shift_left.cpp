//
//  main.cpp
//  calc
//
//  Created by pook on 6/11/18.
//  Copyright © 2018 pook. All rights reserved.
//

#include <iostream>

int countNumber(int n) { // 자릿수를 세는 함수
    int RESULT = 0;
    while (n != 0) {
        n /= 10;
        RESULT += 1;
    }
    return RESULT;
}

int main(int argc, const char * argv[]) {
    std::string a = argv[1];
    int b = atoi(argv[1]);
    int c = atoi(argv[2]);
    int n = countNumber(b);
    std::rotate(a.begin(), a.begin() + c, a.end());
    for (int i=1; i<=c; i++){
        a[n-i] = '0';
    }
    std::printf("%s\n", a.c_str());
    return 0;
}
