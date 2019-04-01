# Python 연습문제 1

2018227 정보보안암호수학과 김진우의 과제입니다.

Python 3.7.3 (macOS) 기준으로 작동합니다.

## 윤년 판별 (leap_year.py)

[leap_year.py로 이동하기](leap_year.py)

### Usage

    `$ /usr/local/bin/python3.7 ./leap_year.py
    Leap year determination (20182217)

    commands:    
    -c, --current   determine that current year is a leap year    
    -y, --year      determine its a leap year`

**leap_year.py**는 입력한 년도의 윤년 판별, 그리고 현재가 윤년인지 판별할 수 있습니다. `printLeapYear` 함수가 입력된 년도가 윤년인지 판단합니다. 또한 윤년 판별의 이유도 표시해 줍니다.


### Example

▼ 현재 (2019년 기준)이 윤년인지 판단

    `$ /usr/local/bin/python3.7 ./leap_year.py -c
    2019 is not a leap year. (reason: 2019 modulo 4 is not 0.)`

    `$ /usr/local/bin/python3.7 ./leap_year.py --current
    2019 is not a leap year. (reason: 2019 modulo 4 is not 0.)`


▼ 1999년이 윤년인지 판단

    `$ /usr/local/bin/python3.7 ./leap_year.py -y 1999
    1999 is not a leap year. (reason: 1999 modulo 4 is not 0.)`

▼ 2040년이 윤년인지 판단

    `$ /usr/local/bin/python3.7 ./leap_year.py -y 2040
    2040 is a leap year. (reason: 2040 modulo 4 is 0.)`

▼ 2100년이 윤년인지 판단

    `$ /usr/local/bin/python3.7 ./leap_year.py -y 2100
    2100 is not a leap year. (reason: 2100 modulo 100 is 0.)`

▼ 2400년이 윤년인지 판단

    `$ /usr/local/bin/python3.7 ./leap_year.py -y 2400
    2400 is a leap year. (reason: 2400 modulo 400 is 0.)`

## 피라미드 인쇄 (pyramid.py)

[pyramid.py로 이동하기](pyramid.py)

### Usage

    `$ /usr/local/bin/python3.7 ./pyramid.py
    Pyramid creation (20182217)

    commands:    
    -n, --row     row of pyramid you want    
    --random      random pyramid. You can set range. (example: ./[file].py --random 5 means row is less than 5.)`

**pyramid.py**는 입력된 높이만큼의 피라미드를 인쇄하며, 지정된 범위 내에서 생성된 무작위 높이로 피라미드를 인쇄할 수 있습니다. `printPyramid` 함수가 피라미드를 인쇄합니다.

### Example
    
▼ 5줄만큼의 피라미드를 인쇄 
    
    `$ /usr/local/bin/python3.7 ./pyramid.py -n 5
        *
       ***
      *****
     *******
    *********`
    
    `$ /usr/local/bin/python3.7 ./pyramid.py --row 5
        *
       ***
      *****
     *******
    *********`
    
▼ 1~6 사이인 무작위 높이의 피라미드를 인쇄
     
     `$ /usr/local/bin/python3.7 ./pyramid.py  --random 6
     random number: 4
        *
       ***
      *****
     *******`
     
## References

- [Leap year/Algorithm](https://en.wikipedia.org/wiki/Leap_year#Algorithm)

- [How to use sys.argv in Python](https://www.pythonforbeginners.com/system/python-sys-argv)

- [python 3.6 displaying IndexError while using sys.argv
](https://stackoverflow.com/questions/48036417/python-3-6-displaying-indexerror-while-using-sys-argv)

- [How to get the current date and time in Python](https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/)

- [Python SyntaxError: invalid syntax end=''
](https://stackoverflow.com/questions/20073639/python-syntaxerror-invalid-syntax-end)
