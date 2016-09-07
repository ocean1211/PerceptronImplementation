from random import choice 
from numpy import array, dot, random 
unit_step = lambda x: 0 if x < 0 else 1 

training_data = [ 
	(array([0,0,1]), 0), 
	(array([0,1,1]), 1), 
	(array([1,0,1]), 1), 
	(array([1,1,1]), 1), 
] 

w = random.rand(3) 
#w = [0, 0, 0]
errors = [] 
eta = 1 
n = 10000

for i in xrange(n): 
	choices = choice(training_data) 
	#print choices
	x, expected = choices
	print x
	result = dot(w, x) 
	#print result
	error = expected - unit_step(result) 
	errors.append(error) 
	#print errors
	w += eta * error * x 
	#print w

for x, _ in training_data: 
	result = dot(x, w) 
	print("{}: {} -> {}".format(x[:2], result, unit_step(result)))