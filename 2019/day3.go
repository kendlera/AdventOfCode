package main 

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"sort"
)

func parseInput() [][]string {
	dat, err := ioutil.ReadFile("input.txt")
    if err != nil {
    	fmt.Println(err)
    	return nil
    }
    wires := strings.Split(string(dat), "\r\n")
    var coords = [][]string{}
    coords = append(coords, strings.Split(wires[0], ","))
    coords = append(coords, strings.Split(wires[1], ","))
    return coords
}

func getPoints(directions []string) [][3]int {
	// takes in input for a wire, returns pairs of coordinates where it turns
	lastPoint := [3]int {0,0,0}
	allPoints := [][3]int{}
	newPoint := [3]int {0,0,0}
	currDist := 0
	allPoints = append(allPoints, lastPoint)
	for _, dir := range directions {
		dist, _ := strconv.Atoi(dir[1:])
		currDist += dist
		if strings.HasPrefix(dir, "R") {
			newPoint = [3]int {lastPoint[0]+dist, lastPoint[1], currDist}
		} else if strings.HasPrefix(dir, "U") {
			newPoint = [3]int {lastPoint[0], lastPoint[1]+dist, currDist}
		} else if strings.HasPrefix(dir, "L") {
			newPoint = [3]int {lastPoint[0]-dist, lastPoint[1], currDist}
		} else { // down
			newPoint = [3]int {lastPoint[0], lastPoint[1]-dist, currDist}
		}
		allPoints = append(allPoints, newPoint)
		lastPoint = newPoint
	}
	return allPoints
}

func myAbs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}

func main() {
	coords := parseInput()
	wire1Points := getPoints(coords[0])
	wire2Points := getPoints(coords[1])
	intercepts := []int {}
	for idx1, _ := range wire1Points {
		if (idx1 == len(wire1Points)-1) {break}
		// figure out if moving from wire1Points[idx] to wire1Points[idx+1]
		// crosses any of wire2Points - add to intercepts if relevant
		for idx2, _ := range wire2Points {
			if (idx2 == len(wire2Points)-1) { break }
			if (wire1Points[idx1][0] == wire1Points[idx1+1][0]) {
				// wire1 has a vertical line
				if wire2Points[idx2][1] == wire2Points[idx2+1][1] {
					// wire2 has a horizonal line! check if these cross
					potentialIntercept := [2]int {wire1Points[idx1][0], wire2Points[idx2][1]}
					minx := wire2Points[idx2][0]
					maxx := wire2Points[idx2+1][0]
					if maxx < minx {
						maxx = minx
						minx = wire2Points[idx2+1][0]
					}
					miny := wire1Points[idx1][1]
					maxy := wire1Points[idx1+1][1]
					if maxy < miny {
						maxy = miny
						miny = wire1Points[idx1+1][1]
					}
					if ((potentialIntercept[0] >= minx) && (potentialIntercept[0] <= maxx) && (potentialIntercept[1] >= miny) && (potentialIntercept[1] <= maxy)) {
						// they cross!
						wire1Dist := wire1Points[idx1][2] + myAbs(wire1Points[idx1][1] - potentialIntercept[1])
						wire2Dist := wire2Points[idx2][2] + myAbs(wire2Points[idx2][0] - potentialIntercept[0])
						// intercepts = append(intercepts, potentialIntercept)
						intercepts = append(intercepts, wire1Dist+wire2Dist)
					}
				}
			} else {
				// wire1 has a horizontal line
				if wire2Points[idx2][0] == wire2Points[idx2+1][0] {
					// wire2 has a vertical line! check if these cross
					potentialIntercept := [2]int {wire2Points[idx2][0], wire1Points[idx1][1]}
					miny := wire2Points[idx2][1]
					maxy := wire2Points[idx2+1][1]
					if maxy < miny {
						maxy = miny
						miny = wire2Points[idx2+1][1]
					}
					minx := wire1Points[idx1][0]
					maxx := wire1Points[idx1+1][0]
					if maxx < minx {
						maxx = minx
						minx = wire1Points[idx1+1][0]
					}
					if ((potentialIntercept[0] >= minx) && (potentialIntercept[0] <= maxx) && (potentialIntercept[1] >= miny) && (potentialIntercept[1] <= maxy)) {
						// they cross!
						wire1Dist := wire1Points[idx1][2] + myAbs(wire1Points[idx1][0] - potentialIntercept[0])
						wire2Dist := wire2Points[idx2][2] + myAbs(wire2Points[idx2][1] - potentialIntercept[1])
						// intercepts = append(intercepts, potentialIntercept)
						intercepts = append(intercepts, wire1Dist+wire2Dist)
					}
				}
			}
		}
	}
	/* manhattans := []int {}
	for _, options := range intercepts {
		manDist := myAbs(options[0]) + myAbs(options[1])
		manhattans = append(manhattans, manDist)
	} 
	sort.Ints(manhattans)
	fmt.Println(manhattans) */
	sort.Ints(intercepts)
	fmt.Println(intercepts)
}