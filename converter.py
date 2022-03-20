from PIL import Image
# gets the image from the input path, or throws errors if
# path does not exist or is not appropriate file type;
# dumps image data into approprate data structure
# https://pythonspot.com/image-data-and-operations/
def getFile(inp):
    pass

# turns the image into black and white
def decolorize():
    pass

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
    inp = input("Enter a file path: ")
    getFile(inp)
    decolorize()
    fillCharMat()
    printMatrix()


main()  