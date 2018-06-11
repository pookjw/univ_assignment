# calc

국민대학교 김진우의 기초프로그래밍 과제입니다. C++과 shell 언어를 통해 제작된 계산기이며, 아래 연산들을 지원합니다.

    (01) a + b       : INTEGER ADDITION

    (02) a - b       : INTEGER SUBTRACTION

    (03) a * b       : INTEGER MULIPLICATION

    (04) a * a       : INTEGER SQUARING

    (05) a = q*b + r : INTEGER DIVISION

    (06) a mod b     : INTEGER MODULAR

    (07) a^n         : INTEGER EXPONENTIATION

    (08) a^n mod m   : INTEGER MODULAR EXPONENTIATION

    (09) gcd(a,b)    : INTEGER GCD

    (10) lcm(a,b)    : INTEGER LCM

    (11) is_prime(a) : INTEGER IS PRIME?

    (12) sqrt(a)     : INTEGER SQUARE ROOT

    (13) rand(a)       : INTEGER RANDOM NUMBER LESS THAN a

    (14) a & b       : BITSTRING AND

    (15) a | b       : BITSTRING OR

    (16) a ^ b       : BITSTRING XOR

    (17) a <<  r, a >>  r : BITSTRING LEFT/RIGHT SHIFT

    (18) a <<< r, a >>> r : BITSTRING LEFT/RIGHT ROTATION

    (19) w(a)        : BITSTRING HAMMING WEIGHT

    (20) len(a)       : BITSTRING BIT LENGTH

    (21) hex(a)      : BITSTRING HEXADECIMAL REPRESENTATION

    (22) bin(a)       : BITSTRING BINARY REPRESENTATION

    (23) bit(a, i)   : BITSTRING i-TH BIT

# To-Do (Version 1.0)

현재 macOS만 지원합니다. macOS Mojave 10.14 Beta (18A293u)와 Xcode 10.0 beta (10L176w)에서 테스트 했습니다.

그렇기에 [바이너리 (링크)](https://github.com/pookjw/univ_assignment/tree/master/기초프로그래밍/project/bin)들은 `Mach-O 64-bit executable x86_64`로 컴파일 되었습니다. Linux와 Windows Subsystem for Linux에서도 지원하고 싶으나... 시간이 안 될 것 같네요 ㅠㅠ 시간되면 하는 걸로...

아직까지는 23개의 연산 중 8번까지만 지원합니다. 마감일 전까지 해야죠...

# How to run

- macOS

Terminal 실행

`cd univ_assignment/기초프로그래밍/project`

`chmod +x calc.sh`

`./calc.sh`
