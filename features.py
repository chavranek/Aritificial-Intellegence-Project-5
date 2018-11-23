class features:
    def getFeatures(self):
        sixFeatures = []
        sixFeatures.append(self.symmetry_density())
        sixFeatures.append(self.density())
        self.to_grey()
        avgVert, maxVert = self.maxAndAverageVertical()
        sixFeatures.append(avgVert)
        sixFeatures.append(maxVert)
        avgHor, maxHor = self.maxAndAveragevertical()
        sixFeatures.append(avgHor)
        sixFeatures.append(maxVert)