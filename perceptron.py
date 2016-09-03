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
	# removing the negative makes it more reasonable but is it right?
	result = y[j] * np.dot(w[j], x[j]) + b[j]
	print "f(w, b)(x) calculation: ", result
	if result > 0:
		return False
	else:
		return True

def perceptron():
	print "\n"
	for i in range(len(x) - 20):
		reweight = determine(i)
		if reweight:
			recalc(i)
		else:
			w.append(w[i])
			b.append(b[i])

		print "interation: ", i
		print "reweight:", reweight
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

print "done training"

numoftrue = 0
numoffalse = 0

#i = 80
for i in range(80, 100):
	print "test: ", i
 	w.append(w[i])
	b.append(b[i])
	print x[i]
	result = determine(i)
	print "result", result, "\n\n"
	if result:
		numoftrue += 1
	else:
		numoffalse += 1

print numoffalse, numoftrue
print "percentage correctly classified: ", 100 * (numoffalse / 20), "%"




