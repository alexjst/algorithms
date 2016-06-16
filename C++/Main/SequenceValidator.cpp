#include "SequenceValidator.h"

#include <vector>
#include <algorithm>

typedef int8_t BYTE;

using namespace std;

int ones(BYTE input) {
    int count = 0;
    for (int i = 1; i <= 8; i++) {
        if (((input >> (8 - i)) & 1) == 1)
            count++;
        else
            break;
    }
    return count;
}

bool isValid(vector<int8_t> input) {
    int numbytes = 0;
    for (int i = 0; i < input.size(); i++) {
        numbytes = ones(input[i]);
        switch (numbytes) {
        case 0: continue;
        case 1: numbytes--;
        default: if (numbytes!=0) return false;
        }
    }
    return (numbytes == 0);
}

void SequenceValidator::run()
{

}
