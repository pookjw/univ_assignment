//
//  main.cpp
//  calc
//
//  Created by pook on 6/11/18.
//  Copyright © 2018 pook. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    std::string a = argv[1];
    int b = atoi(argv[2]);
    std::rotate(a.rbegin(), a.rbegin() + b, a.rend());
    for (int i=0; i<b; i++){
        a[i] = '0';
    }
    std::printf("%s\n", a.c_str());
    return 0;
}
