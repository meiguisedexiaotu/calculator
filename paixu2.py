x = [ 1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
for i in range(0,10):
	for n in range(0,10):
	    if x [i] < x [n]:
		   a = x [i]
		   x [i] = x [n]
		   x [n] = a
print x	