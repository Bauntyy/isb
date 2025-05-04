#include <fstream>
#include <iostream>
#include <random>
#include <string>

/*
* Generates a pseudorandom binary sequence of a specified length
* @param length Length of a binary sequence in bits
* @return String of binary sequence
*/
std::string generateRandomSequence(int length) {
	std::string seq;
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<> distr(0, 1);

	for (size_t i = 0; i < length; ++i) {
		seq += std::to_string(distr(gen));
	}
	return seq;
}

int main() {
	const int binaryLength = 128;
	std::string binarySequence = generateRandomSequence(binaryLength);
	std::cout << binarySequence;
	return 0;
}