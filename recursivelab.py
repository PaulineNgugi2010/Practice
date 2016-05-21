def recursive_factorial(a):
	factorial = 1
	for i in range(1, a +1):
			factorial *=i
			
	return factorial

print recursive_factorial(4)