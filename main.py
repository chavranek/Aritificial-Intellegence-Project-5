from mnist import MNIST

def main():
    '''main function that will do things'''
    mndata = MNIST('samples')


    #loading the images from mnist
    trainImages, trainLabels = mndata.load_training()

    testImages, testLabels = mndata.load_testing()


if __name__ == "__main__":
    main()

