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

	number_map := map[string]string{
		"one":   "one1one",
		"two":   "two2two",
		"three": "three3three",
		"four":  "four4four",
		"five":  "five5five",
		"six":   "six6six",
		"seven": "seven7seven",
		"eight": "eight8eight",
		"nine":  "nine9nine",
	}

	content := string(file)
	codes := strings.Split(content, "\n")

	l := len(codes)
	numbers := make([]uint64, l)

	for _, str := range codes {
		for k, v := range number_map {
			str = strings.ReplaceAll(str, k, v)
		}
		temp := ""
		for _, char := range str {
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
