#include <iostream>
#include <bitset>

using namespace std;

long long generate_value(long long seed, long long factor, long long modulo) {
	// cout << seed << " x " << factor << " % " << modulo << endl;
	long long product = seed * factor;
	// cout << product << endl;
	return product % modulo;
}

bool judge_pairs(long long val1, long long val2) {
	long long grabber = 65535; 	// 16 bits of all 1s
	// cout << val1 << " : " << hex << val1 << endl;
	long long comp1 = val1 & grabber;
	// cout << comp1 << " : " << hex << comp1 << endl;
	long long comp2 = val2 & grabber;
	return (comp1 == comp2);
}

int part_one() {
	long long seed1 = 883;
	long long seed2 = 879;
	long long mod = 2147483647;
	long long factor1 = 16807;
	long long factor2 = 48271;
	int matches = 0;
	for (int i = 0; i < 40000000; i++) {
		seed1 = generate_value(seed1, factor1, mod);
		seed2 = generate_value(seed2, factor2, mod);
		if (judge_pairs(seed1, seed2)) { 
			matches++; 
		}
	}
	return matches;
}

int part_two() {
	long long seed1 = 883;
	long long seed2 = 879;
	long long mod = 2147483647;
	long long factor1 = 16807;
	long long factor2 = 48271;
	int matches = 0;
	for (int i = 0; i < 5000000; i++) {
		do {
			seed1 = generate_value(seed1, factor1, mod);
		} while ((seed1 % 4) != 0);
		do {
			seed2 = generate_value(seed2, factor2, mod);
		} while ((seed2 % 8) != 0);
		if (judge_pairs(seed1, seed2)) { 
			matches++; 
		}
	}
	return matches;
}

int main() {
	/* int ans = part_one();
	cout << ans << " matches found" << endl; */
	int ans = part_two();
	cout << ans << " matches found" << endl;
	return 0;
}