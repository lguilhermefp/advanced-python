def myFunction(arg1, arg2=None):
	"""myFunction(arg1, arg2=None) --> print arguments

	Parameters:
	arg1: the first argument
	arg2: the second argument (optional)
	"""
	print(arg1, arg2)



def main():
	print(myFunction.__doc__)



if __name__ == "__main__":
	main()
