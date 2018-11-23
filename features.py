class features:
	def __init__(self, image):
		img = image
		greyImage = image.copy()

	def density(self):
		return sum(image) / len(image)

	def symetry_density(self):
		x = 0
		i = 0 
		while i < len(self.img):
			for j in range( 0, 28):
				if(self.img[j+i] ^ self.img[(27 - j) + i]) == 0:
					x += 1
			i += 28

		return x / 748

	def to_grey(self):
		for i in range( 0, len(self.img)):
			if self.img[i] >= 128:
				self.greyImage[i] = 0
			elif self.img[i] == 128:
				self.greyImage[i] = 1
		#return self.greyImage
	
	def maxAndAverageVertical(self):
		maxVertical = 0
		totalVertical = 0
		numChanges = 0
		verticalList = []
		for i in range(0, 28):
			j = i
			while j < len(self.greyImage):
				verticallist.append(self.greyImage[j])
				j += 28
			
			for k in range(1,len(verticalList)):
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
				if horizontallist[k-1] != horizontalList[k]:
					numChanges += 1

			maxHorizontal = max(maxHorizontal, numChanges)
			totalHorizontal += numChanges
		
			horizontalList = []
			numChanges = 0
			i += 28

		averageHorizontal = totalHorizontal / 28
		return averageHorizontal, maxHorizontal

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
