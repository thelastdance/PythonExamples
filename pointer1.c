#include <stdio.h>

// finding sum and absolute difference between two numbers.

// int *p = &val ==> assigning memory adress of value.

// *p return the value reflected by val.

void update(int *a,int *b) {
    int number1 = *a;
    int number2 = *b;

    int out1 = number1+number2;
    int out2 = abs(number1-number2);

    printf("%d\n%d",out1,out2);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    

    return 0;
}
