from PIL import Image

#@ # $ % ? * + ; : , .
charDict = {
    0.1: '.',
    0.2: ':',
    0.3: ';',
    0.4: '+',
    0.5: '*',
    0.6: '?',
    0.7: '%',
    0.8: '$',
    0.9: '#',
    1.0: '@',
}

#use Pillow convert method with option L to
#convert image to greyscale -SH
def decolorize(image):
    return image.convert("L")

#resize image to limit text file size -SH
def resize(image, n_width = 50):
    width, height = image.size
    n_height = int(n_width * height / width)
    return image.resize((n_width, n_height))

# initialize character matrix
def initCharMat(x, y):
    return [[' ' for i in range(x)] for j in range(y)]

# takes a float value and searches the dictionary for the
#  first char with greater value
def valToChar(val):
    for i in charDict:
        if val <= i:
            return charDict[i]
    print("Error: given bad val")
    exit()


# fill in character matrix according to image data
def fillCharMat(x, y, image):
    mat = initCharMat(x, y)
    px = image.load()
    # first, get the highest valued pixel
    maxPix = 0
    for i in range(x):
        for j in range(y):
            if px[i, j] > maxPix:
                maxPix = px[i, j]
    
    for i in range(0, y-1):
        for j in range(0, x-1):
            intensity = float(px[j, i] / maxPix)
            c = valToChar(intensity)
            mat[i][j] = c
    return mat



# print the matrix
def printMatrix(x, y, mat):
    for j in range(0, y-1):
        line = ""
        for i in range(0, x-1):
            line += mat[j][i]
            line += mat[j][i]
        print(line)


def main():
    #previous getFile() function -SH    
    path = input("Enter the path to the image : \n")
    image = 0
    try:
        image = Image.open(path)
    except:
         print(path, "Unable to find image")
         exit()
    #get resize size
    try:
        size = int(input("Enter image resize (small~25; large~60): "))
    except:
        print("Size must be an integer.")
        exit()
    # change '25' to make different size
    image = resize(image, size)
    (x, y) = image.size
    image = decolorize(image)
    mat = fillCharMat(x, y, image)
    printMatrix(x, y, mat)


main()  