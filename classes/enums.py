from enum import Enum, unique, auto

@unique
class Fruit(Enum):
	APPLE = 1
	BANANA = 2
	ORANGE = 3
	TOMATE = 4	
	PEAR = auto()

def main():
	# print(Fruit.APPLE)
	# print(type(Fruit.APPLE))
	# print(repr(Fruit.APPLE))

	# print(Fruit.APPLE.name, Fruit.APPLE.value)
	# print(Fruit.PEAR.name, Fruit.PEAR.value)

	characters = {}
	characters[Fruit.BANANA] = "mr. girafales"
	print(characters[Fruit.BANANA])


if __name__ == "__main__":
	main()