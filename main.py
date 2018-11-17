#from PIL import Image
from mnist import MNIST
import random

'''def to_grey(image):
    im = image.open
    width, height = im.size()
    pixels = im.load()
    pixels = image

    for i in range(0, width):
        for j in range(0, height):
            if(pixels[i][j] >= 128):
                pixels[i][j] == 0

            if(pixels[i][j] <= 128):
                pixels[i][j] == 1
    return pixels'''

def to_grey(greyImage):
    '''images loaded in from the mnist data set are already lists
        so we can just iterate through it like a list'''
    for i in range(0, len(greyImage)):
        if greyImage[i] >= 128:
            greyImage[i] = 1

        elif greyImage[i] < 128:
            greyImage[i] = 0

    print(len(greyImage))
    return greyImage

'''def symmetry_dens(image):

    im = Image.open(image)

    # open reverse
    #rev_im = Image.open(image)'''

def specificDigits(labels,images, cls1, cls2):
    '''this function will grab the two desired image classes and output the
    new corresponding label and image arrays
    '''

    specLabels = []
    specImages = []
    for i in range(len(labels)):
        if labels[i] == cls1 or labels[i] == cls2:
            specLabels.append(labels[i])
            specImages.append(images[i])

    return specLabels, specImages

def main():
    '''main function'''

    mndata = MNIST('samples')


    #loading the images from mnist
    trainImages, trainLabels = mndata.load_training()

    testImages, testLabels = mndata.load_testing()

    onesAndFivesLabels, onesAndFivesImages = specificDigits(trainLabels, trainImages, 1, 5)

    index = random.randrange(0, len(onesAndFivesLabels))  # choose an index ;-)
    print(mndata.display(onesAndFivesImages[index]))

    print(onesAndFivesLabels[index])

    image2 = onesAndFivesImages[0]

    image2 = to_grey(image2)

    print(image2)

if __name__ == "__main__":
    main()

