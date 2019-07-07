def find_min(ls):
	min = ls[0]
	ind_min = 0
	for i in range(len(ls)):
		if ls[i] < min:
			min = ls[i]
			ind_min = i
	return ind_min 

print("\nsorting is starting")

ls = generate_list(10)
sorted_list = []

for i in range(len(ls)):
	min = find_min(ls)
	sorted_list.append(ls[min])
	ls.remove(ls[min])
print(f"sorted list is {sorted_list}")
	