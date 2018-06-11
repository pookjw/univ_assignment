//
//  main.cpp
//  calc
//
//  Created by pook on 6/11/18.
//  Copyright © 2018 pook. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int c = 1;
    for (int i = 1; i <= b; i++) {
        c *= a;
    }
    printf("%d\n", c);
    return 0;
}
