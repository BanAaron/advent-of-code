package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	partOne()
	partTwo()
}

func partOne() {
	file, err := os.Open("2021/02/data")
	checkError(err)

	defer func() {
		err := file.Close()
		checkError(err)
	}()

	var position [2]int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, " ")
		dir, val := split[0], split[1]
		num, err := strconv.Atoi(val)
		checkError(err)

		switch dir {
		case "forward":
			position[0] += num
		case "up":
			position[1] -= num
		default:
			position[1] += num
		}
	}

	fmt.Printf("position: %v, result: %d\n", position, position[0]*position[1])
}

func partTwo() {
	file, err := os.Open("2021/02/data")
	checkError(err)

	defer func() {
		err := file.Close()
		checkError(err)
	}()

	var position [3]int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, " ")
		dir, val := split[0], split[1]
		num, err := strconv.Atoi(val)
		checkError(err)

		switch dir {
		case "forward":
			position[0] += num
			position[1] += position[2] * num
		case "up":
			position[2] -= num
		default:
			position[2] += num
		}
	}

	fmt.Printf("position: %v, result: %d\n", position, position[0]*position[1])
}
