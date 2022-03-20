import cv2
import numpy as np
#Pillow must be installed before following import will resolve: -SH
import PIL.Image


# gets the image from the input path, or displays error
# message if image cannot be found; -SH
# dumps image data into approprate data structure
# https://pythonspot.com/image-data-and-operations/

#moved getFile() to main() -SH

#use Pillow convert method with option L to
#convert image to greyscale -SH
def decolorize(image):
    return image.convert("L")

#resize image to limit text file size -SH
def resize(image, n_width = 50):
    width, height = image.size
    n_height = n_width * height / width
    return image.resize((n_width, n_height))

# initialize character matrix
def initCharMat():
    pass 

# fill in character matrix according to image data
def fillCharMat():
    initCharMat()
    pass 

# print the matrix
def printMatrix(mat):
    pass

def main():
    #previous getFile() function -SH    
    path = input("Enter the path to the image : \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to finde image")
        
    #use resize variable to resize image
    image = resize(image)

    decolorize()
    fillCharMat()
    printMatrix()


main()  