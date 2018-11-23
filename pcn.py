import numpy as np

class perceptron:
	def __init__(self, inputs, targets):
		
		"""" Constructor """

		""" Set up input dimension """
		if np.ndim(inputs) > 1:
			self.nIn = np.shape(inputs)[1]
		else:
			self.nIn = 1
		
		""" Set up output dimension """
		if np.ndim(targets) > 1:
			self.nOut = np.shape(targets)[1]
		else:
			self.nOut = 1

		self.nData = np.shape(inputs)[0]


		""" Init weights: W = random(inputSize, outPutSize) * 0.1 - 0.05  """
		self.weights = np.random.rand(self.nIn + 1, self.nOut) * 0.1 - 0.05
		
	""" Train perceptron """
	def perceptronTrain(self, inputs, targets, eta, epochs):
		#Add inputs that match the bias node
		biasNode = -np.ones((self.nData,1))
		inputs = np.concatenate((inputs, biasNode), axis = 1)
		
		#Training 
		change = range(self.nData)
		
		for epoch in range(epochs):
			self.activations = self.perceptronFire(inputs)

			#transpose the matrix 
			transpose = np.transpose(inputs)
			
			#get difference between results vs wanted results
			res = self.activations - targets
			
			#update weights
			self.weights -= eta * np.dot(transpose, res)		
			
			#we might want randomize our orders again

		return self.weights;
			

	""" Run the perceptron foward  aka activation functon"""
	def perceptronFire(self, inputs):
		#compute the activation function 
		activations = np.dot(inputs, self.weights)
		
		#Threshold the results
		return np.where(activations > 0, 1, 0)

	def confusionMatrix(self, inputs, targets):
		#add inputs that match the bias node
		print("hi")
		biasNode = -np.ones((self.nData,1))
		print("Bias node length is: ", len(biasNode))
		print("Input node length is: ", len(inputs))
		inputs = np.concatenate((inputs, biasNode), axis = 1)
		outputs = np.dot(inputs, self.weights)
		
		nClasses = np.shape(targets)[1]
		if nClasses == 1:
			nClasses = 2
			outputs = np.where(outputs > 0, 1, 0)
		else:
			# 1->N encodings
			outputs = np.argmax(outputs, 1)
			targets = np.argmax(targets, 1)
		confusionM = np.zeros((nClasses, nClasses))

		for i in range( nClasses ):
			for j in range( nClasses ):
				confusionM[i][j] = np.sum(np.where(outputs == i, 1, 0) * np.where(targets == j, 1, 0))
		
		#print(confusionM)
		#print( np.trace(confusionM) / np.sum(confusionM) )
