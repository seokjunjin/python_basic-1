#include <iostream>

char byte = 0b10010001;
byte &= 0b11100010;

std::cout << byte << std::endl;
