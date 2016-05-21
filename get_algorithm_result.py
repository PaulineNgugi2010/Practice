def get_algorithm_result(alist):
	Largest = alist[0]

	for i in alist:
		if Largest >= i:
			Largest = i
	return i

print get_algorithm_result([45, 78, 89, 300])



def prime_number(a):
	lower = 0;
	upper = len(a)
	for i in range (lower, upper):
		if (i %  upper ) == 0:
				break
	else:
		return "Prime Numbers are:" , i
print prime_number([3, 4, 5])