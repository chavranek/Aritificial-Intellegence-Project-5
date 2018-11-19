from mnist import MNIST
import random


def density(image):
    # input: takes the non modified image with the original
    #        pixel values in it
    return sum(image) / len(image)


def symmetry_density(image):
    # input: grey scale image of 1s and 0s
    # output: average symmetry density
    #
    # reverse the image list and do an XOR comparison
    # on every value in the array. every time the value
    # returned from the XOR is a 0 that means there is
    # a same pixel value and it gets added to the x value to
    # be averaged out once the list has been exhausted

    reflected = list(reversed(image))
    x = 0

    numOnes = sum(image)

    for i in range(0, len(image)):
        # want to add a 1 for every same value found
        # disregarding all 0 0 pairs
        if image[i] == 1 or reflected[i] == 1:
            if not (image[i] ^ reflected[i]):
                x += 1

    return x / numOnes


def to_grey(image):
    # input: original image represented as list
    # output: image converted to grey scale 1s and 0s
    #
    # images loaded in from the mnist data set are already lists
    # so we can just iterate through it like a list changing all values
    # greater than 128 to 0 and all values less than 128 change to 1.
    greyImage = image.copy()
    for i in range(0, len(image)):
        if image[i] >= 128:
            greyImage[i] = 0

        elif image[i] < 128:
            greyImage[i] = 1

    return greyImage


def maxAndAverageVertical(image):
    # input: grey scale image (binary 1 and 0 values only)
    # output: returns the maximum and average vertical intersections
    maxVertical = 0
    totalVertical = 0
    numChanges = 0
    verticalList = []
    for i in range(0, 28):
        j = i
        while j < len(image):
            verticalList.append(image[j])
            j += 28

        # start at 1 so we can evaluate the 1st row
        # evaluate all values to their previous value
        # to see if there was a change
        for k in range(1, len(verticalList)):
            if verticalList[k-1] != verticalList[k]:
                numChanges += 1

        maxVertical = max(maxVertical, numChanges)
        totalVertical += numChanges

        # reset the list and numChanges variables to evaluate the next column
        verticalList = []
        numChanges = 0

    averageVertical = totalVertical/28

    return averageVertical, maxVertical

def specificDigits(labels,images, cls1, cls2):

    # this function will grab the two desired image classes and output the
    # new corresponding label and image arrays

    specLabels = []
    specImages = []
    for i in range(len(labels)):
        if labels[i] == cls1 or labels[i] == cls2:
            specLabels.append(labels[i])
            specImages.append(images[i])

    return specLabels, specImages


def main():

    mndata = MNIST('samples')


    #loading the images from mnist
    trainImages, trainLabels = mndata.load_training()

    testImages, testLabels = mndata.load_testing()

    onesAndFivesLabels, onesAndFivesImages = specificDigits(trainLabels, trainImages, 1, 5)

    index = random.randrange(0, len(onesAndFivesLabels))  # choose an index ;-)
    print(mndata.display(onesAndFivesImages[index]))

    imageCopy1 = onesAndFivesImages[index].copy()

    imageCopy2 = imageCopy1.copy()

    greyImage = to_grey(imageCopy1)

    symmetryAverage = symmetry_density(greyImage)

    densityImage = density(imageCopy2)

    averageVertical, maxVertical = maxAndAverageVertical(greyImage)

    print("Image List Representation = ", imageCopy1)

    print("Image Class =", onesAndFivesLabels[index])

    print("Image Index =", index)

    print("Grey Image =", greyImage)

    print("Symmetry Average =", symmetryAverage)

    print("Average Density =", densityImage)

    print("Average Vertical Intersections =", averageVertical)

    print("Maximum Vertical Intersections =", maxVertical)






if __name__ == "__main__":
    main()

