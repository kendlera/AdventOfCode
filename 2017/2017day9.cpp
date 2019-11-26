#include <iostream>
#include <fstream>
#include <string>
#include <regex>

using namespace std;

int score_groups(string input) {
	int depth = 0;
	int score = 0;
	for (int i = 0; i < input.size(); i++) {
		if (input[i] == '{') {
			depth ++;
		} else if (input[i] == '}') {
			score = score + depth;
			depth--;
		}
	}
	// cout << input << " scored " << score << endl;
	return score;
}

string strip_and_count_garbage(string result) {
	string l_garbage = "<";
	string r_garbage = ">";
	int l_pos, r_pos;
	int total = 0;
	while ((l_pos = result.find(l_garbage)) != std::string::npos) {
		r_pos = result.find(r_garbage); 
		if (r_pos == string::npos) { break; }
		if (r_pos < l_pos) { 
			cout << "can this happen?\n";
			result.erase(r_pos, 1);
			total ++;
			continue;
		}
		total = total + r_pos - l_pos - 1; // -1 because we don't care about brackets.
		result.erase(l_pos, r_pos - l_pos + 1);
	}
	cout << "we counted " << total << " characters" << endl;
	return result;
}

void part_one() {
	ifstream inFile;
	string input;
	/* learning new ways to read from files! */
	inFile.open("input.txt");
	inFile >> input;
	// cout << input << "\n";

	/* remove all exclamation marks followed by 1 char */
	regex e ("!.");
	string result;
	regex_replace (back_inserter(result), input.begin(), input.end(), e, "$2");
	// cout << result << endl;

	/* part_two */
	result = strip_and_count_garbage(result);

	/* remove commas */
	regex e2 (",");
	string groups;
	regex_replace (back_inserter(groups), result.begin(), result.end(), e2, "$2");
	// cout << groups << endl;

	/* count remaining groups */
	int answer = score_groups(groups);
	cout << "score: " << answer << endl;

}


int main() {
	part_one();
	// 455 too low
	return 0;
}