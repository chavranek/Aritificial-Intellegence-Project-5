"""
Authors: Jorge Bautista, Ryan Boyle, Christian Havranek
Class: CS 480 Artificial Intelligence
Professor: Bala Ravikumar
Project: Project 5 MNIST Data Set Classification
"""
from mnist import MNIST

import random
import numpy as np
import pcn as p
import features as feat

def specificDigits(labels,images, cls1, cls2 = None):

    # this function will grab the two desired image classes and output the
    # new corresponding label and image arrays

    specLabels = []
    specImages = []
    for i in range(len(labels)):
        if labels[i] == cls1 or labels[i] == cls2:
            specLabels.append(labels[i])
            specImages.append(images[i])

    return specLabels, specImages


def splitTrainTest(images, labels):
    twentyPercent  = int(len(images) * 0.20)

    trainImages = images[:len(images)-twentyPercent]
    testImages = images[len(images)-twentyPercent:]

    trainLabels = labels[:len(labels)-twentyPercent]
    testLabels = labels[len(labels)-twentyPercent:]

    return trainImages, testImages, trainLabels, testLabels

def guessImage(image, neuralNet, mndata):
    print("Testing on")
    print(mndata.display(image))
    iFeatures = feat.features(image)
    deezNuts = []
    deezNuts.append(iFeatures.getFeatures())
    deezNuts = np.array(deezNuts)
    print("Activation function res: ", neuralNet.predictImage(deezNuts))

def main():

    print("Preping Data ...")
    mndata = MNIST('samples')


    #loading the images from mnist
    trainImages, trainLabels = mndata.load_training()
    testImages, testLabels = mndata.load_testing()


    # combining all images into the training data so that we can split the data ourselves
    trainImages += testImages
    trainLabels += testLabels

    onesAndFivesLabels, onesAndFivesImages = specificDigits(trainLabels, trainImages, 1, 5)
    data7Labels, data7Images = specificDigits(trainLabels, trainImages, 7)
    data9Labels, data9Images = specificDigits(trainLabels, trainImages, 9)

    data7TrainIm, data7TestIm, data7TrainLa, data7TestLa = splitTrainTest(data7Images, data7Labels)
    data9TrainIm, data9TestIm, data9TrainLa, data9TestLa = splitTrainTest(data9Images, data9Labels)

    TrainImages = onesAndFivesImages + data7TrainIm + data9TrainIm
    TrainLabels = onesAndFivesLabels + data7TrainLa + data9TrainLa

    TestImages = data7TestIm + data9TestIm
    TestLabels = data7TestLa + data9TestLa

    '''
    print("Number of 7s =", len(data7Images))
    print("20% of 7s =", int(len(data7Images)*.20))
    print("Number of 9s =", len(data9Images))
    print("20% of 9s =", int(len(data9Images)*.20))
    '''

		#Save features
    print("Prepping Featuers")
    trainFeatures = []
    for i in TrainImages:
        iFeatures = feat.features(i)
        trainFeatures.append(iFeatures.getFeatures())

		#intit inputs and targets
    inputs = np.array(trainFeatures)
    targets = [[label] for label in TrainLabels]
    targets = np.array(targets)

		#train data
    print("Training Data")
    perc = p.perceptron(inputs, targets)
    print(perc.perceptronTrain(inputs, targets, 0.1, 10000))
    perc.confusionMatrix(inputs, targets)
    print("Finished Training Data")

    '''
    guessImage(data7Images[0], perc, mndata)
    guessImage(data7Images[9], perc, mndata)
    guessImage(data9Images[0], perc, mndata)
    guessImage(data9Images[2], perc, mndata)
    '''

if __name__ == "__main__":
    main()
