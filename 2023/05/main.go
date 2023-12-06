package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

func getAlmanacData(filename string) ([]int, [][][3]int) {
	file, err := os.Open(filename)
	checkError(err)

	defer func() {
		err := file.Close()
		checkError(err)
	}()

	var seeds []int

	scanner := bufio.NewScanner(file)
	var almanac [][][3]int
	var currentMap [][3]int

	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, "seeds") {
			split := strings.Split(line, " ")[1:]
			for _, str := range split {
				strAsInt, err := strconv.Atoi(str)
				checkError(err)
				seeds = append(seeds, strAsInt)
			}
		}

		if strings.Contains(line, "map") {
			almanac = append(almanac, currentMap)
		}

		var firstChar rune
		if len(line) > 0 {
			firstChar = rune(line[0])
		}
		if unicode.IsDigit(firstChar) {
			var store [3]int
			numbers := strings.Split(line, " ")
			for i, n := range numbers {
				n, err := strconv.Atoi(n)
				checkError(err)
				store[i] = n
			}
			currentMap = append(currentMap, store)
		}
	}
	almanac = append(almanac, currentMap)

	err = scanner.Err()
	checkError(err)

	// remove first element
	almanac = almanac[1:]

	return seeds, almanac
}

func main() {
	seeds, almanac := getAlmanacData("2023/05/data")

	fmt.Printf("seeds: %v\n", seeds)
	fmt.Printf("almanac: %v\n", almanac)
}
