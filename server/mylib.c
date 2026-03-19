#include <stdio.h>

int onePlusOne(int a, int b, char operator) {

        int value1 = 0;
        int value2 = 0;

        switch (operator) {
                case '+':
                        return a + b;
                case '-':
                        return a - b;
                case '/':
                        return a / b;
                case '*':
                        return a * b;
                default:
                        break;
        }

        
}

