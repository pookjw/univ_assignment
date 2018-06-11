//
//  main.cpp
//  calc
//
//  Created by pook on 6/11/18.
//  Copyright © 2018 pook. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    int n = atoi(argv[1]);
    int a;
    int result = 1;
    for (a = 1; a < n; a++)
        result = result * a%n;
    result = result % n;
    if (result == n - 1)
        printf("%d is a prime.\n", n); // 소수
    else
        printf("%d is not a prime.\n", n); // 합성수
    return 0;
}
