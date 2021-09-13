def num_function(num: int) -> str:
	return f"{num + 10}"

def str_function(string: str):
	print(string)

if __name__ == '__main__':
	str_function(num_function(30))