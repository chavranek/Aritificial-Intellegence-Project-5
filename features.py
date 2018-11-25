class features:
    def __init__(self, image):
        self.img = image
        self.greyImage = self.to_grey()

    def density(self):
        return sum(self.img) / len(self.img)

    def symmetry_density(self):
        x = 0
        i = 0
        while i < len(self.img) / 2:
            for j in range(0, 28):
                if (self.img[j + i] ^ self.img[(27 - j) + i]) == 0:
                    x += 1
            i += 28

        return x / 748

    def to_grey(self):
        greyImg = self.img.copy()
       	for i in range(0, len(self.img)):
            if self.img[i] >= 128:
                greyImg[i] = 0
            elif self.img[i] < 128:
                greyImg[i] = 1

        return greyImg

    def maxAndAverageVertical(self):
        maxVertical = 0
        totalVertical = 0
        numChanges = 0
        verticalList = []
        for i in range(0, 28):
            j = i
            while j < len(self.greyImage):
                verticalList.append(self.greyImage[j])
                j += 28

            for k in range(1, len(verticalList)):
                if verticalList[k - 1] != verticalList[k]:
                    numChanges += 1

            maxVertical = max(maxVertical, numChanges)
            totalVertical += numChanges

            verticalList = []
            numChanges = 0

        averageVertical = totalVertical / 28
        return averageVertical, maxVertical

    def maxAndAverageHorizontal(self):
        maxHorizontal = 0
        totalHorizontal = 0
        numChanges = 0
        horizontalList = []

        i = 0
        while i < len(self.greyImage):
            for j in range(i, i + 28):
                horizontalList.append(self.greyImage[j])

            for k in range(1, len(horizontalList)):
                if horizontalList[k - 1] != horizontalList[k]:
                    numChanges += 1

            maxHorizontal = max(maxHorizontal, numChanges)
            totalHorizontal += numChanges

            horizontalList = []
            numChanges = 0
            i += 28

        averageHorizontal = totalHorizontal / 28
        return averageHorizontal, maxHorizontal
    def fourByFourAvg(self):
        avg = []
        shift = 0

        while shift < len(self.greyImage) :
            val = 0
            for i in range(4):
              for j in range(4):
                row = i*28 
                col = j + shift
                val += self.greyImage[row + col]
            avg.append(val / 16)
            shift += 4
            if shift % 28 == 0: #if we reached the end of the image, move to the next 7x7 region
                shift += 84

        return avg
    def getFeatures(self):
            sixFeatures = []
            sixFeatures.append(self.symmetry_density())
            sixFeatures.append(self.density())
            #self.to_grey()
            avgVert, maxVert = self.maxAndAverageVertical()
            sixFeatures.append(avgVert)
            sixFeatures.append(maxVert)
            avgHor, maxHor = self.maxAndAverageHorizontal()
            sixFeatures.append(avgHor)
            sixFeatures.append(maxVert)
            return sixFeatures
