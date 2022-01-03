#include<stdio.h>

int main(void){
    int i=0;

    printf("%d\n",i<<31);  //Pass
    printf("%d\n",i<<32);  //warning: left shift count >= width of type

    return 0;
}
