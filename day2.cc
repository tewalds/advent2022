#include <iostream>
#include <fstream>

int main() {
	std::ifstream infile("day2.txt");
	char a, b;
	int total = 0;
	while (infile >> a >> b) {
		a -= 'A';
		b -= 'X';
		int score = b + 1;
		if (a == b) {
			score += 3;
		} else if (a == (b + 2) % 3) {
			score += 6;
		}
		// std::cout << int(a) << ' ' << int(b) << ' ' << score << std::endl;
		total += score;
	}
	std::cout << total << std::endl;
}