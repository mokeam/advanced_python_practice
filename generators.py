# Sequence 1 to 9,000
import sys

def generator(number):
	for x in range(number):
		yield x ** 3

if __name__ == '__main__':
	values = generator(9000)
	print(next(values))
	print(next(values))
	print(next(values))
	print(sys.getsizeof(values))
	values = generator(900000000)
	print(next(values))
	print(next(values))
	print(next(values))
	print(sys.getsizeof(values))