import os
import numpy as np

x = []
y = []
w = [(0, 0, 0, 0)]
b = [0]


def recalc(k):
	w1 = w[k][0] + x[k][0] * y[k] 
	w2 = w[k][1] + x[k][1] * y[k] 
	w3 = w[k][2] + x[k][2] * y[k] 
	w4 = w[k][3] + x[k][3] * y[k] 
	w.append((w1, w2, w3, w4))
	b.append(b[k] + y[k])

def determine(j):
	yi = np.dot(w[j], x[j]) + b[j]

	if (yi < 0 and y[j] < 0) or (yi > 0 and y[j] > 0):
		return True
	else:
		return False

def perceptron():
	print "\n"
	for i in range(len(x)):
		reweight = determine(i)
		if not reweight:
			recalc(i)
		else:
			w.append(w[i])
			b.append(b[i])

		print reweight
		print "x", x[i]
		print "y", y[i]
		print "w", w[i]
		print "b", b[i]
		print "\n\n"



with open('perceptron.data') as openfileobject:
    for line in openfileobject:
    	print line
    	array = [int(var) for var in line.split(',')]
    	x.append(tuple(array[0:4]))
    	y.append(array[4])

print "done stripping text"

print "starting perceptron algorithm ..."
perceptron()