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
np.set_printoptions(threshold=np.nan)

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

'''Extracts featuures from a dataset of images'''
def extractFeatures(dataSet):
    trainFeatures = []
    for i in dataSet:
        iFeatures = feat.features(i)
        trainFeatures.append(iFeatures.getFeatures())
    return np.array(trainFeatures)

def extractTargets(labels):
    targets = [[label] for label in labels]
    targets = np.array(targets)
    return np.where(targets > 7, 1, 0)

def main():
    print("Prepping Data ...")
    #loading the images from mnist
    mndata = MNIST('samples')
    trainImages, trainLabels = mndata.load_training()
    testImages, testLabels = mndata.load_testing()


    # combining all images into the training data so that we can split the data ourselves
    trainImages += testImages
    trainLabels += testLabels

    #onesAndFivesLabels, onesAndFivesImages = specificDigits(trainLabels, trainImages, 1, 5)
    data7Labels, data7Images = specificDigits(trainLabels, trainImages, 7)
    data9Labels, data9Images = specificDigits(trainLabels, trainImages, 9)

    data7TrainIm, data7TestIm, data7TrainLa, data7TestLa = splitTrainTest(data7Images, data7Labels)
    data9TrainIm, data9TestIm, data9TrainLa, data9TestLa = splitTrainTest(data9Images, data9Labels)

    TrainImages = data7TrainIm + data9TrainIm
    TrainLabels = data7TrainLa + data9TrainLa

    TestImages = data7TestIm + data9TestIm
    TestLabels = data7TestLa + data9TestLa

    '''
    print("Number of 7s =", len(data7Images))
    print("20% of 7s =", int(len(data7Images)*.20))
    print("Number of 9s =", len(data9Images))
    print("20% of 9s =", int(len(data9Images)*.20))
    '''

		#init inputs and targets
    print("Prepping Features")
    inputs = extractFeatures(TrainImages)
    targets = extractTargets(TrainLabels)
    testInputs = extractFeatures(TestImages)
    testTargets = extractTargets(TestLabels)

		#train data
    print("Training Data\n")
    perc = p.perceptron(inputs, targets)
    perc.perceptronTrain(inputs, targets, .5, 10000, testInputs, testTargets)
    perc.confusionMatrix(inputs, targets)

    guessImage(data7Images[1], perc, mndata)
    guessImage(data9Images[0], perc, mndata)

    #Test Perceptron
    #print("\nTesting Perceptron on TestSet")
    #inputs = extractFeatures(TestImages)
    #targets = extractTargets(TestLabels)
    #perc.confusionMatrix(inputs, targets)

if __name__ == "__main__":
    main()
