#include <stdio.h>

int main()
{
    int arr[2][3][3] = {4, 17, 9, 21, 5, 33, 55, 78, 99, 2, 47, 3, 12, 3};
    int(*p)[3][3] = arr;
    printf("%d %d", p[1][0][1], p[0][2][2]);
}
