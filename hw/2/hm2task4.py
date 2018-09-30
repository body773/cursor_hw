
def numbers():
	mylist = []
	for i in range(1,30):
		if i % 3 == 0:
			mylist.append("Fizz")
		elif i % 5 == 0:
			mylist.append("Bizz")
		else:
			mylist.append(i)
	return mylist
print(numbers())

