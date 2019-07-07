a = 'top'
b = 'pop'

if len(a) != len(b):
	raise Error

for i in range(len(a)):
	if a[i] != b[-(i+1)]:
		print("Not equal")
		exit()
print("True")