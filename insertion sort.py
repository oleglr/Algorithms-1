from generate_array import *

ls = generate_list(10)

print(ls)

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
	

sorted_list = insertion(ls)
print(ls)