// HelloWorld.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int main()
{
	// Fibonacci numbers
	printf("- Fibonacci numbers\n");
	int a = 0;
	int b = 1;
	int c = 0;
	int COUNT;
	printf("0 (COUNT=1)\n");
	printf("1 (COUNT=2)\n");
	for (COUNT = 3; COUNT <= 20; COUNT++) {
		// To calculate Fibonacci numbers, we have 3 cases; a+b=c, b+c=a and a+c=b. I calculate these equations until COUNT = 20.
		// First, a+b=c means b is bigger than c. so
		if (b > c) {
			c = a + b;
			printf("%d (COUNT=%d)\n", c, COUNT);
		// Second, b+c=a means c is bigger than a. so
		} else if (c > a) {
			a = b + c;
			printf("%d (COUNT=%d)\n", a, COUNT);
		// Final, a+c=b means a is bigger than b. so
		} else if (a>b) {
			b = a + c;
			printf("%d (COUNT=%d)\n", b, COUNT);
		}
	}

	// 20 primes
	printf("\n- 20 primes\n");
	a = 3;
	printf("2 (COUNT=1)\n");
	for (COUNT = 2; COUNT <= 20;) {
		c = a - 1;
		for (b = 2; a > b; b++) {
			if (a%b == 0) {
				// We didn't learn break yet so I used b = a intead of it. So for will stop the loop becuz condition is a > b.
				// break;
				b = a;
			} else if (b == c) {
				printf("%d (COUNT=%d)\n", a, COUNT); // This is prime number!
				COUNT = COUNT + 1;
			}
		}
		a = a + 1;
	}
    return 0;
}
