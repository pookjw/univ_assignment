// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

// 원래 주석 영어로 썼는데 귀찮아서 한글로 쓴 것도 있음

#include "stdafx.h"

int convertTwoFromTenNum(int n) { // 2진수에서 10진수로 변환
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

int powerNumber(int n) {
	int RETURN = 1;
	int i;
	for (i = 1; i <= n; i++) {
		RETURN *= 2;
	}
	return RETURN;
}

int returnBit(int a, int b) {
	int RESULT;
	int i;
	for (i = 1; i <= b; i++) {
		RESULT = a % 2;
		a /= 2;
	}
	return RESULT;
}

int countNumber(int n) { // 자릿수를 세는 함수
	int RESULT = 0;
	int a = convertTwoFromTenNum(n);
	while (a != 0) {
		a /= 10;
		RESULT += 1;
	}
	return RESULT;
}

int main()
{
	while (true) {
		/*I don't know what does `true` mean exactly, but I used this code when I code .sh script like

		#!/bin/sh
		while(true); do
			: # loop code
		done
		
		So I used this.*/
		bool VERBOSE = false; // countNumer의 출력값 같이 로그를 표시하는 기능임. 보고 싶으면 true로 돌리면 됨
		int a = 0;
		int b = 0;
		int q = 0;
		int r = 0;
		int c = 0;
		int d = 1;
		int e;
		int f;
		int g;
		printf("a = bq + r (a and b must be greater than 0 and a is greater than or equal to b.) Enter a and b.\n");
		printf("Enter a = ");
		scanf_s("%d", &a);
		printf("Enter b = ");
		scanf_s("%d", &b);
		if (a > 0 && b > 0) { // If a and b are greater than 0, implement code.
			c = countNumber(a);
			if (VERBOSE == true) {
				printf("countNumber(%d) = %d\n", a, c);
			}
			for (c >= 0; c--; d++) {
				g = c + 1;
				e = returnBit(a, g);
				if (VERBOSE == true) {
					printf("returnBit(%d, %d) = %d\n", a, g, e);
				}
				r = 2 * r + e;
				if (r >= b) {
					r -= b;
					f = powerNumber(c);
					if (VERBOSE == true) {
						printf("powerNumber(%d) = %d\n", c, f);
					}
					q += f;
				}
			}
			printf("q = %d, r = %d\n\n", q, r);
		}
		else { // If not, print error and loop again.
			printf("a and b are not greater than 0.\n");
		}
	}

}

