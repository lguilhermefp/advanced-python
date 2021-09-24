import numpy as np
import math

def main():
	vector = defineVector()
	indexOfGreaterValue = getIndexOfGreaterValueFromVector(vector)
	average = getAverageFromVector(vector)
	print(vector, indexOfGreaterValue, average)



def defineVector():
	newVector = np.array([0.0] * 10)
	for index, v in enumerate(newVector):
		newVector[index] = associateValueForIndex(index)
	return newVector



def getIndexOfGreaterValueFromVector(vector):
	greaterValue = np.max(vector)
	indexOfGreaterValue = np.where(vector == greaterValue)
	return int(indexOfGreaterValue[0])



def getAverageFromVector(vector):
	totalSum = 0
	for value in vector:
		totalSum += value
	average = round(totalSum / len(vector), 2)
	return average



def associateValueForIndex(x):
	if x % 2 == 0:
		return defineValuesForEvenIndex(x)
	return defineValuesForOddIndex(x)



def defineValuesForEvenIndex(x):
	return 3**x + 7*math.factorial(x)



def defineValuesForOddIndex(x):
	return 2**x + 4*math.log(x)



if __name__ == "__main__":
	main()
