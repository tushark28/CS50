#include <math.h>
#include "helpers.h"
// Convert image to grayscale
int ired(int ci, int arr[], int height)
{

    if (ci == 0)
    {
        arr[0] = 0;
        arr[1] = 1;
        return 2;
    }
    else if (ci == height - 1)
    {
        arr[0] = height - 1;
        arr[1] = height - 2;
        return 2;
    }
    else
    {
        arr[0] = ci;
        arr[1] = ci - 1;
        arr[2] = ci + 1;
        return 3;
    }
}

int jred(int cj, int arr2[], int width)
{

    if (cj == width - 1)
    {
        arr2[0] = width - 1;
        arr2[1] = width - 2;
        return 2;
    }
    else if (cj == 0)
    {
        arr2[0] = 0;
        arr2[1] = 1;
        return 2;
    }
    else
    {
        arr2[0] = cj;
        arr2[1] = cj - 1;
        arr2[2] = cj + 1;
        return 3;
    }
}

void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            int tred = image[i][j].rgbtRed;
            int tgreen = image[i][j].rgbtGreen;
            int tblue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][width - 1 - j].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - 1 - j].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - 1 - j].rgbtBlue;

            image[i][width - 1 - j].rgbtBlue = tblue;
            image[i][width - 1 - j].rgbtGreen = tgreen;
            image[i][width - 1 - j].rgbtRed = tred;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int arr[3];
            int arr2[3];

            int reducedi = ired(i, arr, height);
            int reducedj = jred(j, arr2, width);

            int sumR = 0;
            int sumG = 0;
            int sumB = 0;

            for (int x = 0; x < reducedi; x++)
            {
                for (int y = 0; y < reducedj; y++)
                {
                    sumR += new[arr[x]][arr2[y]].rgbtRed;
                    sumG += new[arr[x]][arr2[y]].rgbtGreen;
                    sumB += new[arr[x]][arr2[y]].rgbtBlue;
                }
            }
            int avgR = round(sumR / (float)(reducedi * reducedj));
            int avgG = round(sumG / (float)(reducedi * reducedj));
            int avgB = round(sumB / (float)(reducedi * reducedj));
            image[i][j].rgbtRed = avgR;
            image[i][j].rgbtGreen = avgG;
            image[i][j].rgbtBlue = avgB;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // int gx[3][3];
    // int gy[3][3];
    // gx[0][0] = -1;
    // gx[0][1] = 0;
    // gx[0][2] = 1;
    // gx[1][0] = -2;
    // gx[1][1] = 0;
    // gx[1][2] = 2;
    // gx[2][0] = -1;
    // gx[2][1] = 0;
    // gx[2][2] = 1;

    // gy[0][0] = -1;
    // gy[0][1] = -2;
    // gy[0][2] = -1;
    // gy[1][0] = 0;
    // gy[1][1] = 0;
    // gy[1][2] = 0;
    // gy[2][0] = 1;
    // gy[2][1] = 2;
    // gy[2][2] = 1;

    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    RGBTRIPLE new[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int arr[3];
            int arr2[3];

            int reducedi = ired(i, arr, height);
            int reducedj = jred(j, arr2, width);

            int sumRx = 0;
            int sumGx = 0;
            int sumBx = 0;

            int sumRy = 0;
            int sumGy = 0;
            int sumBy = 0;

            for (int x = 0; x < reducedi; x++)
            {
                for (int y = 0; y < reducedj; y++)
                {
                            if(i==0 || j==0){
                            int temp1=1+x, temp2=1+y;
                            sumRx += gx[temp1][temp2] * new[arr[x]][arr2[y]].rgbtRed;
                            sumGx += gx[temp1][temp2] * new[arr[x]][arr2[y]].rgbtGreen;
                            sumBx += gx[temp1][temp2] * new[arr[x]][arr2[y]].rgbtBlue;

                            sumRy += gy[temp1][temp2] * new[arr[x]][arr2[y]].rgbtRed;
                            sumGy += gy[temp1][temp2] * new[arr[x]][arr2[y]].rgbtGreen;
                            sumBy += gy[temp1][temp2] * new[arr[x]][arr2[y]].rgbtBlue;

                            }

                            sumRx += gx[x][y] * new[arr[x]][arr2[y]].rgbtRed;
                            sumGx += gx[x][y] * new[arr[x]][arr2[y]].rgbtGreen;
                            sumBx += gx[x][y] * new[arr[x]][arr2[y]].rgbtBlue;

                            sumRy += gy[x][y] * new[arr[x]][arr2[y]].rgbtRed;
                            sumGy += gy[x][y] * new[arr[x]][arr2[y]].rgbtGreen;
                            sumBy += gy[x][y] * new[arr[x]][arr2[y]].rgbtBlue;

                }
            }
            int red = round(sqrt((sumRx * sumRx) + (sumRy * sumRy)));
            if(red> 255){
                image[i][j].rgbtRed = 255;
            }
            else{
            image[i][j].rgbtRed = red;
            }

            int green = round(sqrt((sumGx * sumGx) + (sumGy * sumGy)));
            if(green > 255){
                image[i][j].rgbtGreen = 255;
            }
            else{
            image[i][j].rgbtGreen = green;
            }

            int blue = round(sqrt((sumBx * sumBx) + (sumBy * sumBy)));
            if(blue>255){
                image[i][j].rgbtBlue = 255;
            }
            else{
            image[i][j].rgbtBlue = blue;
            }

        }
    }

    return;
}
