package main 

import (
	"fmt"
	"strconv"
	"strings"
	"io/ioutil"
)
func parseInput() []int {
	dat, err := ioutil.ReadFile("input.txt")
    if err != nil {
    	fmt.Println(err)
    	return nil
    }
    arr := strings.Split(string(dat), ",")
    var intified = []int{}
    for _, stringCodes := range arr {
        intCode, err := strconv.Atoi(stringCodes)
        if err != nil {
            panic(err)
        }
        intified = append(intified, intCode)
    }
    return intified
}

func parseOpcode(opcode int) (int, int, int) {
	strValue := strconv.Itoa(opcode)
	length := len(strValue)
	op, _ := strconv.Atoi(string(strValue[length-1]))
	param1, param2 := 0, 0
	if length == 4 {
		param1, _ = strconv.Atoi(string(strValue[1]))
		param2 = 1 // if it's a four digit value, this has to be 1
	} else {
		param1 = 1 // if it's a three digit value, this has to be 1
	}
	return param1, param2, op
}

func main() {
	codes := parseInput()
	currPos := 0
	currCode := codes[currPos]
	mode1, mode2, opcode, val1, val2 := 0, 0, 0, 0, 0
	for currCode != 99 {
		opcode = codes[currPos]
		if opcode > 4 {
			// it has specific parameter/immediate modes
			mode1, mode2, opcode = parseOpcode(opcode)
		} else {
			// clear out any previous codes
			mode1, mode2 = 0, 0
		}
		if opcode == 1 {
			// addition
			val1 = codes[currPos+1]
			if mode1 == 0 {
				val1 = codes[val1]
			} 
			val2 = codes[currPos+2]
			if mode2 == 0 {
				val2 = codes[val2]
			}
			codes[codes[currPos+3]] = (val1 + val2)
			fmt.Printf("%d + %d stored at %d\n", val1, val2, codes[currPos+3])
			currPos += 4
		} else if opcode == 2 {
			// multiplication
			val1 = codes[currPos+1]
			if mode1 == 0 {
				val1 = codes[val1]
			} 
			val2 = codes[currPos+2]
			if mode2 == 0 {
				val2 = codes[val2]
			}
			codes[codes[currPos+3]] = (val1 * val2)
			fmt.Printf("%d * %d stored at %d\n", val1, val2, codes[currPos+3])
			currPos += 4
		} else if opcode == 3 {
			// accept input
			val1 = codes[currPos+1]
			fmt.Printf("Storing 1 at %d\n", val1)
			codes[val1] = 5 // the puzzle told us our input was 5
			currPos += 2
		} else if opcode == 4 {
			// print output
			val1 = codes[currPos+1]
			if mode1 == 0 {
				val1 = codes[val1]
			} 
			fmt.Printf("Output: %d\n", val1)
			currPos += 2
		} else if opcode == 5 {
			// jump if true
			val1 = codes[currPos+1]
			if mode1 == 0 {
				val1 = codes[val1]
			} 
			val2 = codes[currPos+2]
			if mode2 == 0 {
				val2 = codes[val2]
			}
			if val1 != 0 {
				fmt.Printf("True Jumping to %d\n", val2)
				currPos = val2
			} else {
				currPos += 3
			}
		} else if opcode == 6 {
			// jump if false
			val1 = codes[currPos+1]
			if mode1 == 0 {
				val1 = codes[val1]
			} 
			val2 = codes[currPos+2]
			if mode2 == 0 {
				val2 = codes[val2]
			}
			if val1 == 0 {
				fmt.Printf("False Jumping to %d\n", val2)
				currPos = val2
			} else {
				currPos += 3
			}
		} else if opcode == 7 {
			// less than
			val1 = codes[currPos+1]
			if mode1 == 0 {
				val1 = codes[val1]
			} 
			val2 = codes[currPos+2]
			if mode2 == 0 {
				val2 = codes[val2]
			}
			if val1 < val2 {
				codes[codes[currPos+3]] = 1
			} else {
				codes[codes[currPos+3]] = 0
			}
			currPos += 4
		} else if opcode == 8 {
			// equal to 
			val1 = codes[currPos+1]
			if mode1 == 0 {
				val1 = codes[val1]
			} 
			val2 = codes[currPos+2]
			if mode2 == 0 {
				val2 = codes[val2]
			}
			if val1 == val2 {
				codes[codes[currPos+3]] = 1
			} else {
				codes[codes[currPos+3]] = 0
			}
			currPos += 4
		} else {
			fmt.Printf("Bad Opcode at Position %d: %d", currPos, codes[currPos])
			return
		}
		currCode = codes[currPos]
	}
}