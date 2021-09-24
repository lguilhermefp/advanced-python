import numpy as np
import math
import pandas as pd

def main():
	print('execucao do desafio 1:\n')
	vector = defineVector()
	indexOfGreaterValue = getIndexOfGreaterValueFromVector(vector)
	average = getAverageFromVector(vector)
	print("vetor:", vector, "\nposicao de seu maior valor:", indexOfGreaterValue, "\nmedia de seus valores:", average)


	print('\n\n\nexecucao do desafio 2\n')
	df = pd.read_csv('investigados.csv', sep=';', index_col=[0])
	TransformTable(df)
	df = df[df != df.at["Soma", "Soma"]]
	df.to_csv('investigados_totais.csv', sep=';')
	print("table created")



	print('\n\n\nexecucao do desafio 3\n')
	print('type the value to calculate the square root')
	number = float(input())
	sqrt = calculateSqrt(number)
	print(sqrt)


# challenge 1

def defineVector():
	newVector = np.array([0.0] * 10)
	for index, v in enumerate(newVector):
		newVector[index] = associateValueAtIndex(index)
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



def associateValueAtIndex(x):
	if x % 2 == 0:
		return defineValuesForEvenIndex(x)
	return defineValuesForOddIndex(x)



def defineValuesForEvenIndex(x):
	return 3**x + 7*math.factorial(x)



def defineValuesForOddIndex(x):
	return 2**x + 4*math.log(x)



# challenge 2

def TransformTable(df):
	cleanDF(df)
	convertDFFromObjectToFloat(df)
	addSumColumn(df)
	convertDFFromFloatToCurrency(df)



def cleanDF(df):
	dropEmptyColumns(df)
	dropEmptyRows(df)



def convertDFFromObjectToFloat(df):
	partidos = list(df.columns)
	for partido in partidos:
		df[partido] = df[partido].str.replace(',', '.')
		df[partido] = df[partido].astype(float)



def addSumColumn(df):
	partidos = list(df.columns)
	sumColumn = len(partidos)+1
	df.loc[sumColumn] = df.sum()
	df.rename({sumColumn: "Soma"}, axis=0, inplace=True)
	df["Soma"] = df.sum(axis=1)



def convertDFFromFloatToCurrency(df):
	columns = list(df.columns)
	for column in columns:
		convertColumnFromFloatToCurrency(df, column)


	
def dropEmptyColumns(df):
	emptyColumns = [col for col in df.columns if df[col].isnull().all()]
	df.drop(emptyColumns,
		axis=1,
		inplace=True)



def dropEmptyRows(df):
	df.dropna(
		axis=0,
		inplace=True)



def convertColumnFromFloatToCurrency(df, column):
	df[column] = df[column].apply(lambda x: "${0:,.2f}".format(x))
	df[column] = df[column].astype(object)

	invertPointsAndCommas(df, column)



def invertPointsAndCommas(df, column):
	df[column] = df[column].str.replace('.', 'foo', regex=True)
	df[column] = df[column].str.replace(',', '.', regex=True)
	df[column] = df[column].str.replace('foo', ',', regex=True)



# challenge 3

def calculateSqrt(number):
	sqrt = str(number**(1/2))
	sqrt = sqrt.replace('j', 'i')
	return sqrt



if __name__ == "__main__":
	main()
