/* This C source file demonstrates "if-else if-else" and "switch-case-default" paradigms. */
#include <stdio.h>

int main() {
    int a, b;
    printf("Part 1 of our program: judging which number is larger with if-else \n");
    printf("Input an integer number:\n");
    scanf(" %d", &a);
    printf("Input another integer numbrer:\n");
    scanf(" %d", &b);

    if (a>b) { printf("a is larger!\n"); }
    else if (a<b) { printf("b is larger!\n"); }
    else { printf("a is equal to b\n"); }

    printf("\nPart 2 of our program: switch-case.\n");
    printf("\nHow do you want to operate on the two previous numbers:\n");
    char op; scanf(" %c",&op);
    switch (op) {
        case '+': printf("Result is %d\n", a + b); break;
        case '-': printf("Result is %d\n", a - b); break;
        case '*': printf("Result is %d\n", a * b); break;
        case '/':
            if (b!=0) {
                printf("Result is %d\n", a / b);
            } else {
                printf("Cannot devide by zero!");
            }
            break;
        default:
            printf("Invalid input for operator:%c", op);
        }

        int sum, diff;
game:
    printf("\nNow let's play a game.\nThink of two numbgers in your mind...\n");
    printf("First, please tell me the sum of these two numbers:\n");
    scanf("%d", &sum);
    printf("Now tell me the difference of these two numbers:\n");
    scanf("%d", &diff);
    if ( (sum+diff)%2 != 0 ) {
        printf("You must have performed the wrong calculations! Try again:");
        goto game;
    }
    printf("Haha, I know these two numbers now: %d and %d!\n", (sum+diff)/2, (sum-diff)/2);
askAgain:
    printf("Do you want to play again? [y/n]\n");
    char c;
    scanf(" %c", &c);
    if (c=='y' || c=='Y') {
        goto game;
    } else if (c=='n' || c=='N') {
        return 0;
    } else {
        goto askAgain;
    }
}