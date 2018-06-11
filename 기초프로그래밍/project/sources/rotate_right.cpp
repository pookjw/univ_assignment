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
    std::rotate(a.rbegin(), a.rbegin() + b, a.rend()); // int화 시켜서 입력
    std::printf("%s\n", a.c_str());
    return 0;
}
