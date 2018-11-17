from mnist import MNIST
import random

def getLabelIndicees(labels, cls1, cls2):
    '''this function will grab the two desired image classes and output the
    new corresponding label and image arrays
    ------------------WARNING---------------------
    not finished yet
    '''

    specLabels = []
    specImages = []
    for i in range(len(labels)):
        if labels[i] == cls1 or labels[i] == cls2:
            specLabels.append(i)

    return specLabels, specImages

def main():
    '''main function that will do things'''
    #christians branch

    mndata = MNIST('samples')


    #loading the images from mnist
    trainImages, trainLabels = mndata.load_training()

    testImages, testLabels = mndata.load_testing()

    index = random.randrange(0, len(testImages))  # choose an index ;-)
    print(mndata.display(testImages[index]))


if __name__ == "__main__":
    main()

