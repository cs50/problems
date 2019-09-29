#include <stdio.h>
#include <stdlib.h>

#include "helpers.h"

#define GRAYSCALE 0
#define SEPIA 1
#define REFLECT 2
#define BLUR 3
#define EDGES 4

RGBTRIPLE pixel(int r, int g, int b);
void print_pixel(RGBTRIPLE p);
void print_image(int rows, int cols, RGBTRIPLE img[rows][cols]);

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        return 1;
    }

    // Determine which test to run
    int function = atoi(argv[1]);
    int test = atoi(argv[2]);

    // Image with three rows of solid colors
    RGBTRIPLE img1[3][3];
    for (int i = 0; i < 3; i++) {
        img1[0][i] = pixel(0xff, 0, 0);
        img1[1][i] = pixel(0, 0xff, 0);
        img1[2][i] = pixel(0, 0, 0xff);
    }

    // Image with varying colors
    RGBTRIPLE img2[3][3];
    img2[0][0] = pixel(10, 20, 30);
    img2[0][1] = pixel(40, 50, 60);
    img2[0][2] = pixel(70, 80, 90);
    img2[1][0] = pixel(110, 130, 140);
    img2[1][1] = pixel(120, 140, 150);
    img2[1][2] = pixel(130, 150, 160);
    img2[2][0] = pixel(200, 210, 220);
    img2[2][1] = pixel(220, 230, 240);
    img2[2][2] = pixel(240, 250, 255);

    // Larger image
    RGBTRIPLE img3[4][4];
    img3[0][0] = pixel(10, 20, 30);
    img3[0][1] = pixel(40, 50, 60);
    img3[0][2] = pixel(70, 80, 90);
    img3[0][3] = pixel(100, 110, 120);
    img3[1][0] = pixel(110, 130, 140);
    img3[1][1] = pixel(120, 140, 150);
    img3[1][2] = pixel(130, 150, 160);
    img3[1][3] = pixel(140, 160, 170);
    img3[2][0] = pixel(195, 204, 213);
    img3[2][1] = pixel(205, 214, 223);
    img3[2][2] = pixel(225, 234, 243);
    img3[2][3] = pixel(245, 254, 253);
    img3[3][0] = pixel(50, 28, 90);
    img3[3][1] = pixel(0, 0, 0);
    img3[3][2] = pixel(255, 255, 255);
    img3[3][3] = pixel(85, 85, 85);

    // 1x2 row
    RGBTRIPLE row2[1][2];
    row2[0][0] = pixel(255, 0, 0);
    row2[0][1] = pixel(0, 0, 255);

    // 1x3 row
    RGBTRIPLE row3[1][3];
    row3[0][0] = pixel(255, 0, 0);
    row3[0][1] = pixel(0, 255, 0);
    row3[0][2] = pixel(0, 0, 255);

    if (function == GRAYSCALE) {
        switch (test)
        {
            case 0:
            {
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(20, 40, 90);
                grayscale(1, 1, img);
                print_image(1, 1, img);
                break;
            }

            case 1:
            {
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(27, 28, 28);
                grayscale(1, 1, img);
                print_image(1, 1, img);
                break;
            }

            case 2:
            {
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(50, 50, 50);
                grayscale(1, 1, img);
                print_image(1, 1, img);
                break;
            }

            case 3:
            {
                grayscale(3, 3, img1);
                print_image(3, 3, img1);
                break;
            }

            case 4:
            {
                grayscale(3, 3, img2);
                print_image(3, 3, img2);
                break;
            }

            case 5:
            {
                grayscale(4, 4, img3);
                print_image(4, 4, img3);
                break;
            }
        }
    }

    else if (function == SEPIA) {
        switch (test)
        {
            case 0:
            {
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(20, 40, 90);
                sepia(1, 1, img);
                print_image(1, 1, img);
                break;
            }

            case 1:
            {
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(27, 28, 28);
                sepia(1, 1, img);
                print_image(1, 1, img);
                break;
            }

            case 2:
            {
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(50, 50, 50);
                sepia(1, 1, img);
                print_image(1, 1, img);
                break;
            }

            case 3:
            {
                sepia(3, 3, img1);
                print_image(3, 3, img1);
                break;
            }

            case 4:
            {
                sepia(3, 3, img2);
                print_image(3, 3, img2);
                break;
            }

            case 5:
            {
                sepia(4, 4, img3);
                print_image(4, 4, img3);
                break;
            }
        }
    }

    else if (function == REFLECT) {
        switch (test)
        {
            case 0:
            {
                reflect(1, 2, row2);
                print_image(1, 2, row2);
                break;
            }

            case 1:
            {
                reflect(1, 3, row3);
                print_image(1, 3, row3);
                break;
            }

            case 2:
            {
                reflect(3, 3, img1);
                print_image(3, 3, img1);
                break;
            }

            case 3:
            {
                reflect(3, 3, img2);
                print_image(3, 3, img2);
                break;
            }

            case 4:
            {
                reflect(4, 4, img3);
                print_image(4, 4, img3);
                break;
            }
        }
    }

    else if (function == BLUR) {
        switch (test)
        {
            case 0:
            {
                blur(3, 3, img2);
                print_pixel(img2[1][1]);
                break;
            }

            case 1:
            {
                blur(3, 3, img2);
                print_pixel(img2[0][1]);
                break;
            }

            case 2:
            {
                blur(3, 3, img2);
                print_pixel(img2[0][0]);
                break;
            }

            case 3:
            {
                blur(3, 3, img2);
                print_image(3, 3, img2);
                break;
            }

            case 4:
            {
                blur(4, 4, img3);
                print_image(4, 4, img3);
                break;
            }
        }
    }

}

RGBTRIPLE pixel(int r, int g, int b)
{
    RGBTRIPLE p;
    p.rgbtRed = r;
    p.rgbtGreen = g;
    p.rgbtBlue = b;
    return p;
}

void print_pixel(RGBTRIPLE p)
{
    printf("%i %i %i\n", p.rgbtRed, p.rgbtGreen, p.rgbtBlue);
}

void print_image(int rows, int cols, RGBTRIPLE img[rows][cols])
{
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            print_pixel(img[i][j]);
}

