package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	file, err := os.ReadFile("2023/01/data")
	check(err)

	content := string(file)
	codes := strings.Split(content, "\n")

	l := len(codes)
	numbers := make([]uint64, l)

	for _, v := range codes {
		temp := ""
		for _, char := range v {
			if unicode.IsDigit(char) {
				temp += string(char)
			}
		}

		if len(temp) == 1 {
			res, err := strconv.ParseUint(temp+temp, 10, 64)
			check(err)
			numbers = append(numbers, res)
		} else if len(temp) > 1 {
			firstChar := string(temp[0])
			lastChart := string(temp[len(temp)-1])
			res, err := strconv.ParseUint(firstChar+lastChart, 10, 64)
			check(err)
			numbers = append(numbers, res)
		}
	}

	var res uint64
	for _, n := range numbers {
		res += n
	}
	fmt.Println(res)
}
