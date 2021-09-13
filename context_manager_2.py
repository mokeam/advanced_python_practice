from contextlib import contextmanager

@contextmanager
def open_managed_file(file_name):
	f = open(file_name,'w')
	try:
		yield f
	finally:
		f.close()

if __name__ == '__main__':
	with open_managed_file('notes.txt') as f:
		f.write('some todooooo....')