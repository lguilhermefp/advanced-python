import numpy as np
import math

def main():
	vector = defineVector()
	print(vector)



def defineVector():
	newVector = np.array([0.0] * 10)
	for index, value in enumerate(newVector):
		newVector[index] = associateValueForIndex(index)
	return newVector



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
