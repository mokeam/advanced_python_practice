class Vector:
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def __add__(self, new_vector):
		return Vector(self.x + new_vector.x, self.y + new_vector.y)

	def __repr__(self):
		return f"X: {self.x}, Y:{self.y}"

	def __len__(self):
		return 10

	def __del__(self):
		print("Deconstructor executed")

if __name__ == '__main__':
	v1 = Vector(10,20)
	v2 = Vector(50,60)
	v3 = v1 + v2
	v4 = v2 + v3
	print(v3)
	print(len(v3))
	del v4