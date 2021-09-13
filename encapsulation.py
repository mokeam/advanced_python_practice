class Person:
	def __init__(self, name, age, gender):
		self.__name = name
		self.__age = age
		self.__gender = gender

	@property
	def Name(self):
		return self.__name

	@Name.setter
	def Name(self, value):
		self.__name = value

	@property
	def Age(self):
		return self.__age

	@Age.setter
	def Age(self, value):
		self.__age = value

	@property
	def Gender(self):
		return self.__gender

	@Gender.setter
	def Gender(self, value):
		self.__gender = value
	
	@staticmethod
	def start():
		print("Hello World!")

if __name__ == '__main__':
	Person.start()
	p = Person('Mariam',25,'F')
	print(p.Name)
	print(p.Age)
	print(p.Gender)
	p.Name = "Olajumoke"
	p.Age = 26
	p.Gender = "M"
	print(p.Name)
	print(p.Age)
	print(p.Gender)