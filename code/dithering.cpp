#include <stdio.h>
#include <stdlib.h>
#define n 300
#define max_itensity 256
int real[n][n];
int dither[3][3];
int output[n][n];
int main()
{
    printf("Generating random 300x300 image\n");
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
            real[i][j]=rand() % max_itensity;
    }
    printf("Done\n");

    printf("Generating random 3x3 dither matrix\n");
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
            dither[i][j]=rand()%9;
    }
    printf("Done\n");

    printf("Dithering\n");
    for(int y=0; y<n; y++)
    {
        for(int x=0; x<n; x++)
        {
            //printf("%d %d --- ",x,y);
            int i = x % n;
            int j = y % n;
            output[y][x] = (real[y][x] > dither[i][j])? 255 : 0;
        }
    }
    printf("Done\n");

    return 0;
}
