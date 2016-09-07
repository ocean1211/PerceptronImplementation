import os
import numpy as np
from time import sleep

unit_step = lambda x: 0 if x < 0 else 1 
stochastic = 0


x = []
y = []
w = [(0, 0, 0, 0)] * 100
b = [0] * 100

stepsize = 1
convergeiteration = 0
endsum = [0, 0, 0, 0]

def recalc(k):
	if stochastic: 
		w1 = w[k][0] + (stepsize * x[k][0] * y[k]) 
		w2 = w[k][1] + (stepsize * x[k][1] * y[k])
		w3 = w[k][2] + (stepsize * x[k][2] * y[k])
		w4 = w[k][3] + (stepsize * x[k][3] * y[k]) 

		w.append((w1, w2, w3, w4))
		b.append(b[k] + stepsize * y[k])
	else:
		global endsum
		minorsum = [i * y[k] for i in x[k]]
		print minorsum 

		for i in range(4):
			endsum[i] = endsum[i] + minorsum[i]
		print endsum

		if k == 99:
			w1 = w[k][0] + endsum[0]
			w2 = w[k][1] + endsum[1]
			w3 = w[k][2] + endsum[2]
			w4 = w[k][3] + endsum[3]

			global w
			w = [(w1, w2, w3, w4)] * 100
			print w[1]

def determine(j):
	# removing the negative makes it more reasonable but is it right?
	result = (np.dot(w[j], x[j]) + b[j])
	print "f(w, b)(x) calculation: ", result
	if result * y[j] <= 0:
		return True
	else:
		return False

def perceptron():
	print "\n"
	for i in range(len(x)):
		reweight = determine(i)
		if reweight:
			recalc(i)
			global convergeiteration
			convergeiteration = i
		else:
			w.append(w[i])
			b.append(b[i])

		print "convergence: ", convergeiteration
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
while 1:
	perceptron()
	sleep(2)

'''
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
print "percentage correctly classified: ", 100.00 * (numoffalse / 20.00), "%"
print "converged at: ", convergeiteration, "\n"

'''


