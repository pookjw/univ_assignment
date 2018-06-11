//
//  main.cpp
//  calc
//
//  Created by pook on 6/11/18.
//  Copyright © 2018 pook. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    unsigned int v = atoi(argv[1]);
    v = v - ((v >> 1) & 0x55555555);
    v = (v & 0x33333333) + ((v >> 2) & 0x33333333);
    int wt = ((v + (v >> 4) & 0x0f0f0f0f) * 0x01010101) >> 24;
    printf("%d\n", wt);
    return 0;
}
