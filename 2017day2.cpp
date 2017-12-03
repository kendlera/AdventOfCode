/* Day 2 of Advent of Code */
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

void part_one() {
	using namespace std;
    string line;
    char *token;
    int current, max, min;
    int total = 0;
    ifstream myfile ("input.txt");

    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	// std::stringstream token(line);
        	max = 0;
        	min = 99999999;
        	char *cstr = new char[line.length() + 1];
        	strcpy(cstr, line.c_str());
        	token = strtok (cstr, "\t");
            while (token != NULL) {
            	cout << "token: " << token << "\n";
            	current = atoi(token);
            	if (current > max) { max = current; }
            	if (current < min) { min = current; }
            	token = strtok (NULL, "\t");
            }
            total = total + max - min; 
        }
        myfile.close();
    }

    else cout << "Unable to open file"; 

    cout << "Result: " << total << "\n";


}

void part_two() {
	using namespace std;
	string line;
	char *token;
	int current;
	int total = 0;
	bool found;
	ifstream myfile ("input.txt");
    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	vector <int> row; 
        	char *cstr = new char[line.length() + 1];
        	strcpy(cstr, line.c_str()); 	// we have to copy into a non const variable
        	token = strtok (cstr, "\t");
            while (token != NULL) {
            	// cout << "token: " << token << "\n";
            	current = atoi(token);
            	row.push_back(current);
            	token = strtok (NULL, "\t");
            }
            found = false;
         	for (int i = 0; i < row.size(); i++) {
         		for (int j = i+1; j < row.size(); j++) {
         			if ((row.at(i) % row.at(j)) == 0) { 
         				total = total + (row.at(i) / row.at(j));
         				cout << row.at(j) << " divides into " << row.at(i) << "\n";
         				found = true;
         				break;
         			} else if ((row.at(j) % row.at(i)) == 0) { 
         				total = total + (row.at(j) / row.at(i));
         				cout << row.at(i) << " divides into " << row.at(j) << "\n";
         				found = true;
         				break;
         			}
         		}
         		if (found) { break; }
         	}   
        }
        myfile.close();
    }
    cout << "Result " << total << "\n";

}

int main() {
    part_one();
    part_two();
    return 0;
}