package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func grade(score int) string {
	result := ""
	switch {
	//switch后可以没有表达式，默认自动加了break，否则需要fallthrough
	case score < 0 || score > 100:
		result = "数字范围错误"
	case score < 60:
		result = "F"
	case score < 80:
		result = "C"
	case score < 90:
		result = "B"
	case score < 100:
		result = "A"
	case score == 100:
		result = "A+"
	}
	return result
}

func main() {
	const fileName = "01-basic/scores.txt"
	if file, err := os.Open(fileName); err != nil {
		fmt.Println(err)
	} else {
		fileScanner := bufio.NewScanner(file)
		for fileScanner.Scan() {
			score, err := strconv.Atoi(fileScanner.Text())
			result := ""
			if err == nil {
				result = strconv.Itoa(score) + " -> " + grade(score)
			} else {
				result = "非法数字 : " + fileScanner.Text()
			}
			fmt.Println(result)
		}
	}

	fmt.Println(
		grade(0),
		grade(59),
		grade(60),
		grade(82),
		grade(99),
		grade(100),
		// Uncomment to see it panics.
		// grade(-3),
	)
}
