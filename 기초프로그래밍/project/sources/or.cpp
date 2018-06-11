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
    std::string b = argv[2];
    int c = atoi(argv[1]);
    int n = countNumber(c);
    std::string final_key;
    for(int i = 0; i<n; i++)
    {
        final_key[i] = ((a[i]-'0') ^ (b[i]-'0')) + '0'; // int화 시켜서 입력
        if (a[i] == '1' || b[i] == '1' ){
            final_key[i] = '1';
        }else{
            final_key[i] = '0';
        }
        std::cout<<final_key[i];
    }
    printf("\n");
    return 0;
}
