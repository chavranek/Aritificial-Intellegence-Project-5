from mnist import MNIST
import random

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

