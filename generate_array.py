from random import randint

def generate_list(num_elements):
	ls = []

	for _ in range(num_elements):
		ls.append(randint(0, 10))

	return ls