#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>

void part_one() {
	using namespace std;
    string line;
    string delimiter = " ";
    char *token;
    int current, max, min;
    int total = 0;
    size_t pos = 0;
    bool found;
    int lines = 0;
    ifstream myfile ("input.txt");

    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	set<string> row; 
            pos = 0;
            std::string token;
            found = false;
            while ((pos = line.find(delimiter)) != std::string::npos) {
                token = line.substr(0, pos);
                // cout << "token: " << token << "\n";
                if (row.find(token) != row.end()) {
                    total++;
                    cout << "found " << token << " in line " << lines << "\n";
                    found = true;
                    break;
                }
                row.insert(token);
                line.erase(0, pos + 1);
            }
            // cout << "Final? " << line << "\n";
            if (row.find(line) != row.end() && !found) {
                total++;
                cout << "found " << token << " in line " << lines << "\n";
            }
            lines ++;
        }
        myfile.close();
    }
    cout << "Total " << lines - total << "\n";
}


void part_two() {
    using namespace std;
    string line;
    string delimiter = " ";
    char *token;
    int current, max, min;
    int total = 0;
    size_t pos = 0;
    bool found, exist_perms;
    int lines = 0;
    ifstream myfile ("input.txt");

    if (myfile.is_open()) {
        while (getline (myfile,line)) {
            set<string> row; 
            pos = 0;
            std::string token;
            found = false;
            while ((pos = line.find(delimiter)) != std::string::npos) {
                token = line.substr(0, pos);
                exist_perms = true;
                /* sort alphabetically */
                sort(token.begin(), token.end());
                while (exist_perms) {
                    if (row.find(token) != row.end()) {
                        total++;
                        cout << "found " << token << " in line " << lines << "\n";
                        found = true;
                        break;
                    }
                    exist_perms = next_permutation(token.begin(), token.end());
                }
                if (found) { break; }
                row.insert(token);
                line.erase(0, pos + 1);
            }
            if (!found) {
                exist_perms = true;
                sort(line.begin(), line.end());
                while (exist_perms) {
                    if (row.find(line) != row.end() && !found) {
                        total++;
                        cout << "found " << line << " in line " << lines << "\n";
                    }
                    exist_perms = next_permutation(line.begin(), line.end());
                }
            }
            lines ++;
        }
        myfile.close();
    }
    cout << "Total " << lines - total << "\n";
}

int main() {
    // part_one();
    part_two();
    return 0;
}