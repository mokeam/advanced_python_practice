import time

def execution_time(function):
	def wrapper(*args, **kwargs):
		before = time.time()
		function(*args, **kwargs)
		after = time.time()
		function_name = function.__name__
		print(f"{function_name} took {after - before} seconds to execute")
	return wrapper

@execution_time
def loop_function(x):
	result = 1
	for i in range(1,x):
		result *= i
	return result

@execution_time
def count_down(x):
	temp = 0
	for i in range(1,x):
		temp = -i

if __name__ == '__main__':
	loop_function(1000)
	count_down(1000)