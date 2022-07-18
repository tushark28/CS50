#include <math.h>
#include "helpers.h"
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i =0;i<height;i++){
        for(int j=0;j<width;j++){
            int avg = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen)/3.0);
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
    for(int i =0;i<height;i++){
        for(int j=0;j<width/2;j++){
            int tred= image[i][j].rgbtRed;
            int tgreen= image[i][j].rgbtGreen;
            int tblue= image[i][j].rgbtBlue;
            
            image[i][j].rgbtRed = image[i][width -1- j].rgbtRed;
            image[i][j].rgbtGreen = image[i][width -1- j].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width -1- j].rgbtBlue;

            image[i][width -1- j].rgbtBlue = tblue;
            image[i][width -1- j].rgbtGreen = tgreen;
            image[i][width -1- j].rgbtRed = tred;
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
