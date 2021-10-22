class Person():
	def  __init__(self):
		self.fname = "luis"
		self.lname = "guilherme"
		self.age = 20


	def __repr__(self):
		return "<Person Class - fname: {0}, lname: {1}, age: {2}".format(
			self.fname, self.lname, self.age
			)

	
	def __str__(self):
		return "Person ({0} {1} is {2})".format(
			self.fname, self.lname, self.age
		)


	def __bytes__(self):
		val = "Person:{0}:{1}:{2}".format(
			self.fname, self.lname, self.age
		)
		return bytes(val.encode('utf-8'))


def main():
	person = Person()

	print(repr(person))
	print(str(person))
	print("formated: {0}".format(person))
	print(bytes(person))


if __name__ == "__main__":
	main()
