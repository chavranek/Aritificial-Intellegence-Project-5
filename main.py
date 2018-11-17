from PIL import Image
from mnist import MNIST
import random

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

if __name__ == "__main__":
    main()

