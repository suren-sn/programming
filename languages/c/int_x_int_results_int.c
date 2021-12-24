#include<stdio.h>

int main(int argc, char **argv){

    int i=46341;
    long l=46341;
    long exp_result=2147488281;

    printf("Expected result: %ld\n", exp_result);

    if(i*i == exp_result)
        printf("int*int pass\n");
    else
        printf("int*int fail. result:%d\n", i*i);

    if(l*l == exp_result)
        printf("long*long pass. result:%ld\n", l*l);
    else
        printf("long*long fail. result:%ld\n", l*l);

    if(l*i == exp_result)
        printf("long*int pass. result:%ld\n", l*i);
    else
        printf("long*int fail. result:%ld\n", l*i);

    if((long)(i*i) == exp_result)
        printf("(long)(int*int) pass. result:%ld\n", (long)(i*i));
    else
        printf("(long)(int*int) fail. result:%ld\n", (long)(i*i));

    return 0;
}

