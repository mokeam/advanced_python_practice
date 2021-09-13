class ManagedFile:
	def __init__(self, file_name):
		print("Init")
		self.file_name = file_name

	def __enter__(self):
		print("Enter")
		self.file = open(self.file_name,'w')
		return self.file

	def __exit__(self, exc_type, exc_value, exc_traceback):
		if self.file:
			self.file.close()
		if exc_type is not None:
			print("Exception has been handled")
		print("exc:", exc_type, exc_value)
		print("Exit")
		return True

if __name__ == '__main__':
	with ManagedFile('notes.txt') as file:
		print("Do some stuff....")
		file.write('some todo...')
		file.some_method()
	print("continuing")