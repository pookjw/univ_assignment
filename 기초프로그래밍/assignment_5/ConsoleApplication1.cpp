// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int returnMP(int n) {
	int a;
	int b = 1;
	for (a = 1; a <= n; a++)
	{
		b = 2 * b;
	}
	b -= 1;
	return b;
}

int isPrime(int m) {
	int c;
	int result = 1;
	for (c = 1; c < m; c++)
		result = result * c%m;
	result = result % m;
	if (result == m - 1)
		return 1; // 소수
	else
		return 0; // 합성수
}

int main()
{
	int d;
	int e;
	int f = 2;
	int k;
	for (d = 1; d <= 8; f++) {
		if (isPrime(f) == 1) {
			d += 1;
			k = isPrime(f);
			e = returnMP(f);
			printf("%d\n", e);
		}
	}
    return 0;
}

