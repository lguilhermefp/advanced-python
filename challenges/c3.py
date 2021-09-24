def calculateSqrt(number):
	sqrt = str(number**(1/2))
	sqrt = sqrt.replace('j', 'i')
	return sqrt



def main():
	number = float(input())
	sqrt = calculateSqrt(number)
	print(sqrt)



if __name__ == "__main__":
	main()
