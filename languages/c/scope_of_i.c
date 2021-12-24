#include<stdio.h>

int main(void)
{
    int M = 2;
    int i=-10;
    for (int i = 0; i < M; i++)
    {
        printf ("%d\n", i);
    }
    printf ("Out of loop : %d\n", i);
    return 0;
}
