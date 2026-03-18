#include <stdio.h>

int onePlusOne(int a, int b, char operator) {

        switch (operator) {
                case '+':
                        return a + b;
                case '-':
                        return a - b;
                case '*':
                        return a * b;
                case '/':
                        return a / b;
                default:
                        return 1;
                        break;
        }
}

