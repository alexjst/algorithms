#include <stdio.h>

int main() {
    /*
    for (int x=1; x<100; x++) {
        int y = x*3+2;
        if ( (x*5+94) == (y*3) ) {
            printf("x=%d\n", x);
            printf("y=%d\n", y);
            break;
        }
    }
    */

   for (int x = 1; x<100; x++) {
       for (int y = 1; y<100; y++) {
           if ( x*3+2 == y && x*5+94 == y*3) {
                printf("x=%d\n", x);
                printf("y=%d\n", y);
                break;
           }
       }
   }
    return 0;
}