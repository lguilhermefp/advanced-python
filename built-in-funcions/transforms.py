def filterFunc(x):
	if x % 2 == 0:
		return False
	return True



def filterFunc2(x):
	if x.isupper():
		return False
	return True



def squareFunc(x):
	return x**2



def toGrade(x):
	if (x>=90):
		return "A"
	elif (x>=80):
		return "B"
	elif (x>=70):
		return "C"
	elif (x>=65):
		return "D"
	return "F"




def main():
	nums = (1, 9, 4, 5, 13, 26, 381, 410, 58, 47)
	chars = "abcDeFGHiJklmnoP"
	grades = (81, 89, 94, 78, 61, 66, 99, 74)

	# odds = list(filter(filterFunc, nums))
	# print(odds)

	# lowers = list(filter(filterFunc2, chars))
	# print(lowers)

	# squares = list(map(squareFunc, nums))
	# print(squares)

	grades = sorted(grades)
	letters = list(map(toGrade, grades))
	print(letters)



if __name__  == "__main__":
	main()
