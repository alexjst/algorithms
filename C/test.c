/*
 * This is a sample C program
 */

#include <stdio.h>

void printBinary(int num) {
    unsigned long sz = sizeof(num);
    // char* pchar = (char*)malloc(sz+1);
    unsigned long bitsz = sz * 8;
    printf("binary of int %d is: ", num);
    for (int i=bitsz-1; i>=0; i--) {
        printf("%d", (num >> i) & 1);
    }
    printf("\n");
}

int main() {
    int a = 0b100;
    //int b = 0b110;
    printf("sizeof(int)=%ld\n", sizeof(int));
    printf("sizeof(int64)=%ld\n", sizeof(int64_t));
    printf("sizeof(long)=%ld\n", sizeof(long));
    printBinary(7);

    return 0; 
}
