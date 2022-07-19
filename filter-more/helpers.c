#include <math.h>
#include "helpers.h"

// Convert image to grayscale
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
            int sumR = 0;
            int sumG = 0;
            int sumB = 0;
            int count =0;
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    if (i + x >= 0 && i + x < height && j + y >= 0 && j + y < width)
                    {

                        sumR += new[i + x][y + j].rgbtRed;
                        sumG += new[i + x][y + j].rgbtGreen;
                        sumB += new[i + x][j + y].rgbtBlue;
                        count++;
                    }
                }
            }

            int avgR = round(sumR / (float)(count));
            int avgG = round(sumG / (float)(count));
            int avgB = round(sumB / (float)(count));

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

            int sumRx = 0;
            int sumGx = 0;
            int sumBx = 0;

            int sumRy = 0;
            int sumGy = 0;
            int sumBy = 0;

            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    if (i + x >= 0 && i + x < height && j + y >= 0 && j + y < width)
                    {

                        sumRx += gx[x + 1][y + 1] * new[i + x][y + j].rgbtRed;
                        sumGx += gx[x + 1][y + 1] * new[x + i][y + j].rgbtGreen;
                        sumBx += gx[x + 1][y + 1] * new[x + i][y + j].rgbtBlue;

                        sumRy += gy[x + 1][y + 1] * new[x + i][y + j].rgbtRed;
                        sumGy += gy[x + 1][y + 1] * new[x + i][y + j].rgbtGreen;
                        sumBy += gy[x + 1][y + 1] * new[x + i][y + j].rgbtBlue;
                    }
                }
            }

            int red = round(sqrt((sumRx * sumRx) + (sumRy * sumRy)));
            int green = round(sqrt((sumGx * sumGx) + (sumGy * sumGy)));
            int blue = round(sqrt((sumBx * sumBx) + (sumBy * sumBy)));

            image[i][j].rgbtRed = (red > 255) ? 255 : red;
            image[i][j].rgbtGreen = (green > 255) ? 255 : green;
            image[i][j].rgbtBlue = (blue > 255) ? 255 : blue;
        }
    }

    return;
}
