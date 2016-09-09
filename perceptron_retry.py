import os, sys
import numpy as np
from time import sleep

x = []
y = []
w = [0, 0, 0, 0]
b = 0

delta = [0, 0, 0, 0]
deltab = 0

stepsize = 1

done = 1
count = 0
inter_count = 0


def stochastic_perceptron():
	global w
	global b
	global inter_count
	global delta
	global deltab

	global w
	global b
	global inter_count
	global delta
	global deltab

	for i in range(2):
		ui = np.dot(w, x[i]) + b

		if y[i] * ui <= 0:
			inter_count += 1
			for j in range(4):
				w[j] = w[j] -  (stepsize * (delta[j] - (y[i] * x[i][j])))

	print "w: ", w
	print "b: ", b
	if inter_count == 0:
		global done
		done = 0
		print "w: ", w
		print "b: ", b

	print inter_count
	inter_count = 0


def perceptron():
	global w
	global b
	global inter_count
	global delta
	global deltab

	for i in range(2):
		ui = np.dot(w, x[i]) + b

		if y[i] * ui <= 0:
			inter_count += 1
			for j in range(4):
				updelta = delta[j] - (y[i] * x[i][j])
				delta[j] = updelta
				deltab += y[i]

		if i == 1:
			for k in range(4):
				w[k] = w[k] - (stepsize * delta[k] / 4)
			b = stepsize * deltab
			print "w: ", w
			print "b: ", b
			delta = [0, 0, 0, 0]
			deltab = 0
	
	if inter_count == 0:
		global done
		done = 0

	print inter_count
	inter_count = 0


with open('perceptron_copy.data') as openfileobject:
    for line in openfileobject:
    	#print line
    	array = [float(var) for var in line.split(',')]
    	x.append(tuple(array[0:4]))
    	y.append(array[4])

    stepsize = float(sys.argv[2])

print "done stripping text"

print "starting perceptron algorithm ..."

if sys.argv[1] == "stochastic":
	while done == 1:
		stochastic_perceptron()
		#sleep(2)
		count += 1
else:
	while done == 1:
		perceptron()
		#sleep(2)
		count += 1


print "count: ", count
