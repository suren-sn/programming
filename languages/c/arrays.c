#include<stdio.h>
int main(){
    //int *nums = {1,2,3,4,5,6,7};      //Invalid
    int nums[] = {1,2,3,4,5,6,7};       //Valid
    int size = sizeof(nums)/sizeof(int);
    int i;

    for(i=0; i<size; i++){
        printf("%d  ", i);
    }
    printf("\n");
}

