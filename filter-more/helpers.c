#include <math.h>
#include "helpers.h"
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++) // col stands for Column
        {
            //Fetch all RGB values and average it
            float average = round((image[row][col].rgbtRed + image[row][col].rgbtGreen + image[row][col].rgbtBlue) / 3.0);

            //New pixel value
            image[row][col].rgbtRed = average;
            image[row][col].rgbtGreen = average;
            image[row][col].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i =0;i<height;i++){
        for(int j=0;j<width/2;j++){
            int tred= image[i][j].rgbtRed;
            int tgreen= image[i][j].rgbtGreen;
            int tblue= image[i][j].rgbtBlue;
            image[i][j].rgbtRed = image[i][width - j].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - j].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - j].rgbtBlue;
            image[i][width - j].rgbtBlue = tblue;
            image[i][width - j].rgbtGreen = tgreen;
            image[i][width - j].rgbtRed = tred;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
