package main

import (
	"fmt"
	"os"
	"regexp"
	"slices"
	"strconv"
	"strings"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func maxPower(str string, colour string) (int, error) {
	r := regexp.MustCompile("(\\d+)\\s+" + colour)
	// matches returns a slice of string slices
	// [0][0] contains the original string
	// [0][1] contains the value extracted from the regex match
	matches := r.FindAllStringSubmatch(str, -1)

	var numbers []int
	for _, match := range matches {
		num, err := strconv.Atoi(match[1])
		if err != nil {
			return 0, err
		}
		numbers = append(numbers, num)
	}

	return slices.Max(numbers), nil
}

func main() {
	var red, green, blue []int
	var games []string

	file, err := os.ReadFile("2023/02/data")
	check(err)
	data := string(file)
	split := strings.Split(data, "\n")
	// this is essentially pop() from Python
	games = append(games, split[:len(split)-1]...)

	for _, game := range games {
		redPower, err := maxPower(game, "red")
		check(err)
		red = append(red, redPower)

		greenPower, err := maxPower(game, "green")
		check(err)
		green = append(green, greenPower)

		bluePower, err := maxPower(game, "blue")
		check(err)
		blue = append(blue, bluePower)
	}

	var multi []int
	for i := 0; i < len(red); i++ {
		multi = append(multi, red[i]*green[i]*blue[i])
	}

	var result int
	for _, power := range multi {
		result += power
	}

	fmt.Println(result)
}
