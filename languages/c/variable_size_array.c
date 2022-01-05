#include<stdio.h>

void init_variable_size_array(){
    int size=10;
    int array[size] = {0};  //Compile error: variable-sized object may not be initialized
}

int main(void)
{
    int M = 2;
    int arr[M][M];
    int i, j;
    for (i = 0; i < M; i++)
    {
        for (j = 0; j < M; j++)
        {
            arr[i][j] = j;
            printf ("%d ", arr[i][j]);
        }
        printf("\n");
    }

    init_variable_size_array();
    return 0;
}
