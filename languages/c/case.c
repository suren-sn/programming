#include<stdio.h>
#include<ctype.h>

int main()
{
    printf("tolower...\n");
    printf("A : %c\n", tolower('A'));
    printf("a : %c\n", tolower('a'));
    printf("1 : %c\n", tolower('1'));

    printf("toupper...\n");
    printf("A : %c\n", toupper('A'));
    printf("a : %c\n", toupper('a'));
    printf("1 : %c\n", toupper('1'));

    return 0;
}
