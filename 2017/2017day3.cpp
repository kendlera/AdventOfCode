#include <iostream>
#include <math.h>
#include <vector>

void part_one(){
	using namespace std;
	int target = 289326;
	int distance = 1;
	while (true) {
		if (target <= pow((distance*2) - 1, 2)) {
			int ring_max = pow((distance*2) - 1, 2);
			int ring_min = pow(((distance-1)*2) - 1, 2)+1;
			int chunk = (ring_max - ring_min + 1) / 8; // distance from axis
			int position = target - ring_min; // location in the spiral
			cout << "target at distance " << distance << " and location " << position << " out of " << ring_max - ring_min << "!\n";
			cout << (position % chunk) + distance << " steps\n";
			return;
		} else {
			cout << "current count " << pow((distance*2) - 1, 2) << "\n";
		}
		distance ++;

	}
}

int RR = 20000;
int CC = 20000;
std::vector<std::vector<int> > matrix(RR);
int get_sum(std::vector<int> pos) {
	int total = 0;
	total = total + matrix[pos[0]+1][pos[1]+1];
	total = total + matrix[pos[0]+1][pos[1]];
	total = total + matrix[pos[0]+1][pos[1]-1];
	total = total + matrix[pos[0]][pos[1]-1];
	total = total + matrix[pos[0]-1][pos[1]-1];
	total = total + matrix[pos[0]-1][pos[1]];
	total = total + matrix[pos[0]-1][pos[1]+1];
	total = total + matrix[pos[0]][pos[1]+1];
	return total;
}

/*
Right -> 0
Up    -> 1
Left  -> 2
Down  -> 3
*/
int direction = 3;
std::vector<int> next_position(std::vector<int> current) {
	/* determines what the next space of memory is to be filled */
	using namespace std;
	switch(direction) {
		case 0:
		    if (matrix[current[0]][current[1]+1] == 0) {
		    	direction = 1;
		    	current[1]++;
		    } else {
		    	current[0]++;
			}
		    return current;
		case 2:
			if (matrix[current[0]][current[1]-1] == 0) {
				direction = 3;
				current[1]--;
			} else {
				current[0]--;
			}
			return current;
		case 1:
			if (matrix[current[0]-1][current[1]] == 0) {
		    	direction = 2;
		    	current[0]--;
		    } else {
		    	current[1]++;
		    }
		    return current;
		case 3:
			if (matrix[current[0]+1][current[1]] == 0) {
		    	direction = 0;
		    	current[0]++;
		    } else {
		    	current[1]--;
		    }
		    return current;
		default:
			std::cout << "error\n";
			return current;
	}
}

void part_two() {
	int target = 289326;
	int current = 1;
	using namespace std;
	for ( int i = 0 ; i < RR ; i++ ) {
		matrix[i].resize(CC);
	}
	vector<int> pos;
	pos.push_back(RR/2);
	pos.push_back(CC/2);
	matrix[pos[0]][pos[1]] = 1;
	while (current <= target) {
		pos = next_position(pos);
		cout << pos[0] << ", " << pos[1] << "\n";
		current = get_sum(pos);
		matrix[pos[0]][pos[1]] = current;
	}
	cout << "Answer: " << current << "\n";
}

int main(){
	part_one();
	part_two();
	return 0;
}