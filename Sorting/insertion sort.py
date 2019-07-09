from generate_array import generate_list

"""
O(n^2)
"""
def insertion(ls):
	for i in range(1, len(ls)):
		
		current = ls[i]
		pos = i
		while pos > 0 and  ls[pos-1] > current:
			# swap elements
			ls[pos] = ls[pos-1]
			pos -= 1
		ls[pos] = current
	return ls
	

def insertion_acs(ls):
	for i in range(1, len(ls)):
		
		current = ls[i]
		pos = i
		# changes only line below
		while pos > 0 and  ls[pos-1] < current:
			# swap elements
			ls[pos] = ls[pos-1]
			pos -= 1
		ls[pos] = current
	return ls

if __name__ == "__main__":

	ls = generate_list(15)
	print(ls)

	sorted_list = insertion_acs(ls)
	print(ls)