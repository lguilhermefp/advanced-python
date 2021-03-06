import itertools

def testFunction(x):
	return x < 40



def main():
	seq1 = ["joe", "john", "mike"]
	cycle1 = itertools.cycle(seq1)
	# print(next(cycle1))
	# print(next(cycle1))
	# print(next(cycle1))
	# print(next(cycle1))

	count1 = itertools.count(100, 10)
	# print(next(count1))
	# print(next(count1))
	# print(next(count1))

	vals = [10, 20, 30, 40, 50, 40, 30]
	acc = itertools.accumulate(vals)
	# print(list(acc))
	acc = itertools.accumulate(vals, max)
	# print(list(acc))

	x = itertools.chain("ABCD", "1234")
	# print(list(x))

	print(list(itertools.dropwhile(testFunction, vals)))
	print(list(itertools.takewhile(testFunction, vals)))



if __name__ == "__main__":
	main()
