#!/bin/sh
# calc
TOOL_VERSION="1.2"

function showLines(){ # columns 길이에 맞게 선을 출력하는 함수
	PRINTED_COUNTS=0
	COLS=`tput cols`
	if [[ "${COLS}" -ge 1 ]]; then
		while [[ ! $PRINTED_COUNTS == $COLS ]]; do
			printf "${1}"
			PRINTED_COUNTS=$((${PRINTED_COUNTS}+1))
		done
		echo
	fi
}

function grepAnswer(){ # 아래 read에서 받아들인 ANSWER 값을 파싱하는 용도
	echo "${ANSWER}" | grep "${1}"
}

function cutANSWER(){ # 아래 read에서 받아들인 ANSWER 값을 파싱하는 용도
	echo "${ANSWER}" | cut -d"${1}" -f"${2}"
}

clear
while(true); do
	COMMAND=
	read -p "calc-${TOOL_VERSION}$ " ANSWER

	if [[ ! -z "$(grepAnswer "(")" ]]; then # 명령어가 a+b, a-b 형식이 아닌, sum(a,b), sub(a,b) 형식일 경우
		COMMAND="$(cutANSWER "(" "1")" # ( 앞에 있는 명령어를 잘라냄. 예를 들어 sum(6,3)이면 COMMAND=sum
		if [[ -f "bin/${COMMAND}" ]]; then
			ANSWER="$(cutANSWER "(" "2")"
			ANSWER="$(cutANSWER ")" "1")"
			if [[ ! -z "$(grepAnswer ",")" ]]; then
				"bin/${COMMAND}" "$(cutANSWER "," "1")" "$(cutANSWER "," "2")"
			else
				"bin/${COMMAND}" "${ANSWER}"
			fi
		else
			echo "command not found: ${COMMAND}"
		fi
	elif [[ ! -z "$(grepAnswer "exit")" ]]; then
		exit 0
	elif [[ ! -z "$(grepAnswer "clear")" ]]; then
		clear
	elif [[ ! -z "$(grepAnswer "help")" ]]; then
		if [[ ! -z "$(grepAnswer "example")" ]]; then # example은 bin 폴더 안에 있는 파일들이 live로 실행됨
			echo "INPUT				OUTPUT"
			showLines "-"
			for NAME in sum sub mul div mod exp gcd lcm; do
				echo "${NAME}(6,4)			result: $("bin/${NAME}" 6 4)"
				if [[ "${NAME}" == exp ]]; then
					echo "6^4 mod 5			result: $(bin/mod "$(bin/exp 6 4)" 5)"
				fi
			done
			for NAME in is_prime sqrt rand; do
				echo "${NAME}(100)			result: $("bin/${NAME}" 100)"
			done
			for NAME in and or xor; do
				echo "${NAME}(10110, 11011)		result: $("bin/${NAME}" 10110 11011)"
			done
			for NAME in shift_left shift_right rotate_left rotate_right; do
				echo "${NAME}(10110, 2)		result: $("bin/${NAME}" 10110 2)"
			done
			for NAME in hwt len hex bin; do
				echo "${NAME}(8)				result: $("bin/${NAME}" 8)"
			done
			echo "bit(9, 2)			result: $(bin/bit 9 2)"
		else
			echo "sum(a,b)		INTEGER ADDITION (alt command: a+b)"
			echo "sub(a,b)		INTEGER SUBTRACTION (alt command: a-b)"
			echo "mul(a,b)		INTEGER MULIPLICATION (alt command: a*b)"
			echo "div(a,b)		INTEGER DIVISION, it means a=q*b+r and will print q and r. (alt command: a/b)"
			echo "mod(a,b)		INTEGER MODULAR (alt command: a%b)"
			echo "exp(a,b)		INTEGER EXPONENTIATION"
			echo "a^b mod m		INTEGER MODULAR EXPONENTIATION"
			echo "gcd(a,b)		INTEGER GCD"
			echo "lcm(a,b)		INTEGER LCM"
			echo "is_prime(a)		INTEGER IS PRIME?"
			echo "sqrt(a)			INTEGER SQUARE ROOT"
			echo "rand(a)			INTEGER RANDOM NUMBER LESS THAN a"
			echo "and(a,b)		BITSTRING AND (alt command: a&b)"
			echo "or(a,b)			BITSTRING OR (alt command: a|b)"
			echo "xor(a,b)			BITSTRING XOR (alt command: a^b)"
			echo "shift_left(a,r)	BITSTRING LEFT SHIFT (alt command: a<<r)"
			echo "shift_right(a,r)	BITSTRING RIGHT SHIFT (alt command: a>>r)"
			echo "rotate_left(a,r)	BITSTRING LEFT ROTATION (alt command: a<<<r)"
			echo "rotate_right(a,r)	BITSTRING RIGHT ROTATION (alt command: a>>>r)"
			echo "hwt(a)			BITSTRING HAMMING WEIGHT"
			echo "len(a)			BITSTRING BIT LENGTH"
			echo "hex(a)			BITSTRING HEXADECIMAL REPRESENTATION"
			echo "bin(a)			BITSTRING BINARY REPRESENTATION"
			echo "bit(a, i)		BITSTRING i-TH BIT"
			echo "exit			quit tool"
			echo "clear			clear window"
			echo "help [option]		show this message. (option: --example)"
		fi
	# alt command를 인식하는 코드입니다. a+b, a-b 같은 것들.
	elif [[ ! -z "$(grepAnswer "+")" ]]; then #a+b
		bin/sum "$(cutANSWER "+" "1")" "$(cutANSWER "+" "2")"
	elif [[ ! -z "$(grepAnswer "-")" ]]; then #a-b
		bin/sub "$(cutANSWER "-" "1")" "$(cutANSWER "-" "2")"
	elif [[ ! -z "$(grepAnswer "*")" ]]; then #a*b
		bin/mul "$(cutANSWER "*" "1")" "$(cutANSWER "*" "2")"
	elif [[ ! -z "$(grepAnswer "/")" ]]; then #a/b
		bin/div "$(cutANSWER "/" "1")" "$(cutANSWER "/" "2")"
	elif [[ ! -z "$(grepAnswer "%")" ]]; then #a%b
		bin/mod "$(cutANSWER "%" "1")" "$(cutANSWER "%" "2")"
	elif [[ ! -z "$(grepAnswer "^")" && ! -z "$(grepAnswer "mod")" ]]; then # a^b mod m
		NUMBER_1="$(bin/exp "$(cutANSWER "^" "1")" "$(cutANSWER "^" "2")")"
		NUMBER_2="$(cutANSWER "d" "2")"
		bin/mod "${NUMBER_1}" "${NUMBER_2}"
	elif [[ ! -z "$(grepAnswer "&")" ]]; then # a&b
		bin/and "$(cutANSWER "&" "1")" "$(cutANSWER "&" "2")"
	elif [[ ! -z "$(grepAnswer "|")" ]]; then # a|b
		bin/or "$(cutANSWER "|" "1")" "$(cutANSWER "|" "2")"
	elif [[ ! -z "$(grepAnswer "\^")" ]]; then # a^b
		bin/xor "$(cutANSWER "^" "1")" "$(cutANSWER "^" "2")"
	elif [[ ! -z "$(grepAnswer "<<<")" ]]; then # a<<<r
		bin/rotate_left "$(cutANSWER "<" "1")" "$(cutANSWER "<" "4")"
	elif [[ ! -z "$(grepAnswer ">>>")" ]]; then # a>>>r
		bin/rotate_right "$(cutANSWER ">" "1")" "$(cutANSWER ">" "4")"
	elif [[ ! -z "$(grepAnswer "<<")" ]]; then # a<<r
		bin/shift_left "$(cutANSWER "<" "1")" "$(cutANSWER "<" "3")"
	elif [[ ! -z "$(grepAnswer ">>")" ]]; then # a>>r
		bin/shift_right "$(cutANSWER ">" "1")" "$(cutANSWER ">" "3")"
	# END
	elif [[ -z "${ANSWER}" ]]; then
		:
	else
		echo "I can't recognize that command. Sorry."
	fi
done
