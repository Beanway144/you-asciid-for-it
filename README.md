# Image to Ascii Converter
The goal of this program is to turn an input jpg or png into ascii art.

## Current Outlook (updated 3/13/2022:
1. Load and resize image
 - [ [  Load image with Pillow
 - [ ]  Resize image to ensure text file isn't too large

2. Convert image to grayscale
 - [ ] Define ascii conversion list
 - [ ]  Convert existing image to grayscale by pixel

3. Convert each grayscale pixel to corresponding ascii character
 - [ ] Convert individual grayscale images to ascii characters

4. Output image
 - [ ] Print output image to screen
 - [ ] Set default csv file output repository

________________________________________________________________________

## Current Outlook:
1. Take an input image (sehardwick)
- [x] Ask the user for a path to file
- [ ] Make sure the path leads to a jpg, png, etc.
- [ ] Access image data
- [ ] Put RGB data into data structure (like 2d list)

2. Convert all image pixels to black and white (sehardwick)
- [ ] Run through the matrix, taking the average of each R, B, and G
- [ ] Replace RGB data with that average at each pixel

3. Create a matrix of chars depending on RGB value at each pixel (beanway144)
- [ ] Find average of all values
- [ ] Find good range to determine relative strength of character density
- [ ] Depending on resolution specs, get average of multiple pixels
- [ ] Fill in matrix with chars like (space), -, =, $, &, #

4. Print char matrix (beanway144)
- [ ] Compile the matrix into strings
- [ ] Print and finish

## Design Considerations:
- What should the resolution of the final ascii string be? should it be 1/4th the original?
