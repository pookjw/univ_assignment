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
    int gcd, lcm, remainder, numerator, denominator;
    
    if (a > b){
        numerator = a;
        denominator = b;
    }else{
        numerator = b;
        denominator = a;
    }
    remainder = numerator % denominator;
    if (remainder == 0){
        gcd = denominator;
    }else{
        while (remainder != 0){
            remainder = numerator % denominator;
            numerator = denominator;
            denominator = remainder;
        }
        gcd = numerator;
    }
    lcm = a * b / gcd;
    printf("%d\n", lcm);
}
