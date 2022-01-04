#include<stdio.h>

int main(void){
    int addone(int x){
        return x+1;
    }

    int y=100;
    printf("Addone to %d: %d\n", y, addone(y));
    return 0;
}

