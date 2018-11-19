from mnist import MNIST
import random


def density(image):
    # takes the non modified image with the original
    # pixel values in it
    return sum(image) / len(image)


def symmetry_density(image):
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

    # images loaded in from the mnist data set are already lists
    # so we can just iterate through it like a list changing all values
    # greater than 0 to 1 and all values equal to 0 stay zero.
    # we use 0 as the threshold because any value over 0 means there is a
    # mark that is a part of the number even if it is lighter
    greyImage = image.copy()
    for i in range(0, len(image)):
        if image[i] > 0:
            greyImage[i] = 1

        else:
            greyImage[i] = 0

    return greyImage


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

    print("Image List Representation = ", imageCopy1)

    print("Image Class =", onesAndFivesLabels[index])

    print("Image Index =", index)

    print("Grey Image =", greyImage)

    print("Symmetry Average =", symmetryAverage)

    print("Average Density =", densityImage)




if __name__ == "__main__":
    main()

