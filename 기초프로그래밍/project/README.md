# calc

![Image](https://farm2.staticflickr.com/1751/41841805485_3776c17b2a_o.png)

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

# Compatibility

macOS만 지원합니다. macOS Mojave 10.14 Beta (18A293u)와 Xcode 10.0 beta (10L176w)에서 테스트 했습니다.

그렇기에 [바이너리 (링크)](https://github.com/pookjw/univ_assignment/tree/master/기초프로그래밍/project/bin)들은 `Mach-O 64-bit executable x86_64`로 미리 컴파일 되었습니다.

# How to run

- macOS

`$ cd univ_assignment/기초프로그래밍/project`

`$ chmod +x calc.sh`

`$ ./calc.sh`

그러면 `calc.sh`이 실행되며, `help` 명령어로 사용 가능한 명령어 목록을 볼 수 있습니다.

하나하나 다 돌려보기 귀찮으시면 `help --example` 명령어로 일괄적으로 실행시킬 수 있습니다.
