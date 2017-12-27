#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>

using namespace std;

int dist_from_origin(vector<int> coords) {
	if (coords.size() != 3) { cout << "vector is wrong size" << endl; }
	return abs(coords.at(0)) + abs(coords.at(1)) + abs(coords.at(2));
}

map<string, vector<int> > fetch_measurements(string line) {
	map<string, vector<int> > position;
	string separator = ", ";
	string comma = ",";
	string coords, tag;
	int pos;
	while ((pos = line.find(separator)) != string::npos) {
		vector<int> numbers;
		tag = line.substr(0, 1);
		coords = line.substr(3, pos-4);
		line.erase(0, pos+2);
		// cout << coords << " to be processed" << endl;
		while ((pos = coords.find(comma)) != string::npos) {
			// cout << "adding " << coords.substr(0, pos) << endl;
			numbers.push_back(stoi(coords.substr(0, pos)));
			coords.erase(0, pos+1);
		}
		// cout << "adding " << coords << endl;
		numbers.push_back(stoi(coords));
		position[tag] = numbers;
	}
	vector<int> numbers;
	tag = line.substr(0, 1);
	coords = line.substr(3, line.size()-4);
	// cout << coords << " to be processed" << endl;
	while ((pos = coords.find(comma)) != string::npos) {
		// cout << "adding " << coords.substr(0, pos) << endl;
		numbers.push_back(stoi(coords.substr(0, pos)));
		coords.erase(0, pos+1);
	}
	// cout << "adding " << coords << endl;
	numbers.push_back(stoi(coords));
	position[tag] = numbers;
	return position;

}

vector<map<string, vector<int> > > read_input() {
	ifstream myfile ("input.txt");
	string line, vector_str;
	vector<map<string, vector<int> > > particles;
	vector<int> coords; 
    if (myfile.is_open()) {
        while (getline (myfile,line)) {
        	particles.push_back(fetch_measurements(line));
        }
        myfile.close();
    }
    return particles;
}

void part_one() {
	vector<map<string, vector<int> > > particles;
	map<string, vector<int> > measurements;
	int accel_min = 100;
	int slowest, acceleration;
	particles = read_input();
	for (int i = 0; i < particles.size(); i++) {
		measurements = particles.at(i);
		acceleration = dist_from_origin(measurements["a"]);
		if (acceleration < accel_min) {
			accel_min = acceleration;
			slowest = i;
		}
	}
	cout << "slowest particle " << slowest << endl;
}

void sum_vectors(vector<int> &changing, vector<int> &changer) {
	for (int i = 0; i < changing.size(); i++) {
		changing.at(i) = changing.at(i) + changer.at(i);
	}
}

void update_positions(vector<map<string, vector<int> > > &particles) {
	vector<int> changing;
	vector<int> changer;
	map<string, vector<int> > particle;
	for (int i = 0; i < particles.size(); i++) {
		particle = particles.at(i);
		// update velocity
		changing = particle["v"];
		changer = particle["a"];
		sum_vectors(changing, changer);
		particle["v"] = changing;
		// update positions
		changer = changing;
		changing = particle["p"];
		sum_vectors(changing, changer);
		particle["p"] = changing;
		particles.at(i) = particle;
	}
}

void explode_particles(vector<map<string, vector<int> > > &particles) {
	map<string, vector<int> > particle1;
	map<string, vector<int> > particle2;
	vector<int> pos1;
	vector<int> pos2;
	set<int> collided;
	// cout << "checking collisions" << endl;
	for (int i = 0; i < particles.size(); i++) {
		particle1 = particles.at(i);
		pos1 = particle1["p"];
		for (int j = i+1; j < particles.size(); j++) {
			particle2 = particles.at(j);
			pos2 = particle2["p"];
			if ((pos1.at(0) == pos2.at(0)) && (pos1.at(1) == pos2.at(1)) && (pos1.at(2) == pos2.at(2))) {
				collided.insert(i);
				collided.insert(j);
			}
		}
	}
	set<int>::reverse_iterator rit;
	for (rit = collided.rbegin(); rit != collided.rend(); ++rit) {
		cout << "erasing " << *rit << endl;
		particles.erase(particles.begin() + *rit);
	}
}

void part_two() {
	vector<map<string, vector<int> > > particles;
	vector<int> particle_pos;
	particles = read_input();
	bool done = false;
	int num_particles = particles.size();
	int consecutive_misses = 0;
	particle_pos = particles.at(0)["p"];
	cout << particle_pos.at(0) << ", " << particle_pos.at(1) << ", " << particle_pos.at(2) << endl;
	while (!done) {
		update_positions(particles);
		explode_particles(particles);
		particle_pos = particles.at(0)["p"];
		cout << particle_pos.at(0) << ", " << particle_pos.at(1) << ", " << particle_pos.at(2) << endl;
		if (particles.size() == num_particles) {
			// none collided
			consecutive_misses++;
			if (consecutive_misses > 20) { done = true; }
		} else { 
			consecutive_misses = 0; 
			num_particles = particles.size();
		}
	}
	cout << particles.size() << " particles remain" << endl;
}


int main() {
	part_one();
	part_two();
	return 0;
}