#!/bin/sh
# calc
TOOL_VERSION="1.0"

function showLines(){
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

function showPA2C(){
	read -s -n 1 -p "Press any key to continue..."
	echo
}

function grepAnswer(){
	echo "${ANSWER}" | grep "${1}"
}

function cutANSWER(){
	echo "${ANSWER}" | cut -d"${1}" -f"${2}"
}

function loadSettings(){
	if [[ -f /tmp/calc/SHOW_MESSAGE_ON_START ]]; then
		SHOW_MESSAGE_ON_START=$(cat /tmp/calc/SHOW_MESSAGE_ON_START)
	else
		SHOW_MESSAGE_ON_START=true
	fi
	if [[ -f /tmp/calc/VERBOSE ]]; then
		VERBOSE=$(cat /tmp/calc/SHOW_MESSAGE_ON_START)
	else
		VERBOSE=false
	fi
}

function saveSettings(){
	if [[ -d /tmp/calc ]]; then
		rm -rf /tmp/calc
	fi
	mkdir -p /tmp/calc
	echo "${SHOW_MESSAGE_ON_START}" >> /tmp/calc/SHOW_MESSAGE_ON_START
	echo "${VERBOSE}" >> /tmp/calc/VERBOSE
}

loadSettings
if [[ "${SHOW_MESSAGE_ON_START}" == true ]]; then
	clear
	showLines "*"
	echo "calc ${TOOL_VERSION}"
	showLines "-"
	echo "계산기 프로그램입니다."
	echo "덧셈, 뺄셈, 나누기 등을 지원합니다. 예를 들어 \`3 + 4\`를 입력하면 7이 출력됩니다. \`help\` 명령어를 통해 더 많은 명령들을 열람할 수 있습니다."
	echo ""
	echo "국민대학교 20182217 김진우"
	showLines "*"
	read -s -n 1 -p "Press any key to continue..."
fi
clear
while(true); do
	COMMAND=
	read -p "calc-${TOOL_VERSION}$ " ANSWER

	if [[ ! -z "$(grepAnswer "(")" ]]; then
		COMMAND="$(cutANSWER "(" "1")"
		if [[ -f "bin/${COMMAND}" ]]; then
		ANSWER="$(cutANSWER "(" "2")"
		ANSWER="$(cutANSWER ")" "1")"
			"bin/${COMMAND}" "$(cutANSWER "," "1")" "$(cutANSWER "," "2")"
		else
			echo "command not found: ${COMMAND}"
		fi
	elif [[ ! -z "$(grepAnswer "exit")" ]]; then
		exit 0
	elif [[ ! -z "$(grepAnswer "clear")" ]]; then
		clear
	elif [[ ! -z "$(grepAnswer "help")" ]]; then
		if [[ ! -z "$(grepAnswer "example")" ]]; then
			for NAME in sum sub mul div mod exp; do
				echo "${NAME}(5,3)	result: $(bin/${NAME} 5 3)"
				if [[ "${NAME}" == exp ]]; then
					echo "5^3 mod 4	result: $(bin/mod "$(bin/exp 5 3)" 4)"
				fi
			done
		else
			echo "sum(a,b)	INTEGER ADDITION (alt command: a+b)"
			echo "sub(a,b)	INTEGER SUBTRACTION (alt command: a-b)"
			echo "mul(a,b)	INTEGER MULIPLICATION (alt command: a*b)"
			echo "div(a,b)	INTEGER DIVISION, it means a=q*b+r and will print q and r. (alt command: a/b)"
			echo "mod(a,b)	INTEGER MODULAR (alt command: a%b)"
			echo "exp(a,b)	INTEGER EXPONENTIATION (alt command: a^b)"
			echo "a^b mod m	INTEGER MODULAR EXPONENTIATION"
			echo "exit		quit tool"
			echo "clear		clear window"
			echo "settings	show settings"
			echo "help [option]	show this message. (option: --example)"
		fi
	elif [[ ! -z "$(grepAnswer "settings")" ]]; then
		saveSettings
		while(true); do
			clear
			showLines "*"
			echo "SHOW_MESSAGE_ON_START=${SHOW_MESSAGE_ON_START}"
			echo "VERBOSE=${VERBOSE}"
			showLines "-"
			echo "calc's settings will be saved on /tmp/calc. So it will be reset when you erase it."
			echo "Enter value to inverse setting. (true<->false) To quit, enter \`exit\`."
			showLines "*"
			read -p "settings-${TOOL_VERSION}$ " ANSWER
			if [[ ! -z "$(grepAnswer "SHOW_MESSAGE_ON_START")" ]]; then
				if [[ "${SHOW_MESSAGE_ON_START}" == true ]]; then
					SHOW_MESSAGE_ON_START=false
				else
					SHOW_MESSAGE_ON_START=true
				fi
			elif [[ ! -z "$(grepAnswer "VERBOSE")" ]]; then
				if [[ "${VERBOSE}" == true ]]; then
					VERBOSE=false
				else
					VERBOSE=true
				fi
			elif [[ ! -z "$(grepAnswer "exit")" ]]; then
				saveSettings
				clear
				break
			elif [[ ! -z "$(grepAnswer "reset")" ]]; then
				rm -rf /tmp/calc
				loadSettings
			elif [[ -z "${ANSWER}" ]]; then
				:
			else
				echo "I can't recognize that command. Sorry."
			fi
		done
	elif [[ ! -z "$(grepAnswer "+")" ]]; then
		bin/sum "$(cutANSWER "+" "1")" "$(cutANSWER "+" "2")"
	elif [[ ! -z "$(grepAnswer "-")" ]]; then
		bin/sub "$(cutANSWER "-" "1")" "$(cutANSWER "-" "2")"
	elif [[ ! -z "$(grepAnswer "*")" ]]; then
		bin/mul "$(cutANSWER "*" "1")" "$(cutANSWER "*" "2")"
	elif [[ ! -z "$(grepAnswer "/")" ]]; then
		bin/div "$(cutANSWER "/" "1")" "$(cutANSWER "/" "2")"
	elif [[ ! -z "$(grepAnswer "%")" ]]; then
		bin/mod "$(cutANSWER "%" "1")" "$(cutANSWER "%" "2")"
	elif [[ ! -z "$(grepAnswer "^")" && ! -z "$(grepAnswer "mod")" ]]; then
		NUMBER_1="$(bin/exp "$(cutANSWER "^" "1")" "$(cutANSWER "^" "2")")"
		NUMBER_2="$(cutANSWER "d" "2")"
		bin/mod "${NUMBER_1}" "${NUMBER_2}"
	elif [[ ! -z "$(grepAnswer "^")" ]]; then
		bin/exp "$(cutANSWER "^" "1")" "$(cutANSWER "^" "2")"
	elif [[ -z "${ANSWER}" ]]; then
		:
	else
		echo "I can't recognize that command. Sorry."
	fi
done