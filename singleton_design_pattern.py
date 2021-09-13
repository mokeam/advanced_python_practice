from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):

	@abstractstaticmethod
	def print_data():
		""" Implement in child class """

class PersonSingleton(IPerson):

	__instance = None

	@staticmethod
	def get_instance():
		if PersonSingleton.__instance == None:
			PersonSingleton("Defaule Name",0)
		else:
			return PersonSingleton.__instance

	def __init__(self, name, age):
		if PersonSingleton.__instance != None:
			raise Exception("Singletion cannot be instantiated more than once")
		else:
			self.name = name
			self.age = age
			PersonSingleton.__instance = self

	@staticmethod
	def print_data():
		print(f"Name: {PersonSingleton.__instance.name} Age: {PersonSingleton.__instance.age}")

if __name__ == '__main__':
	p = PersonSingleton("Mariam", 25)
	print(p)
	p.print_data()

	p3 = PersonSingleton.get_instance()
	p3.print_data()
