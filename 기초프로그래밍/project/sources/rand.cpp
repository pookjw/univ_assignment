//
//  main.cpp
//  calc
//
//  Created by pook on 6/11/18.
//  Copyright © 2018 pook. All rights reserved.
//

#include <iostream>
#include <time.h>

int main(int argc, const char * argv[]) {
    int n = atoi(argv[1]);
    int rd;
    srand((int)time(NULL));
    for (int i=0; i<=n; i++){
        rd = rand() % n;
    }
    printf("%d\n", rd);
    return 0;
}
