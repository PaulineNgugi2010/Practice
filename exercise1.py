









count = 0
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
	count = count +1
	total = total +itervar

print 'Count: ', count
print 'Total: ', total
print len([3, 41, 12, 9, 74, 15])
print sum([3, 41, 12, 9, 74, 15])






friends = ['Joseph', 'Glen', 'Sally']
for friend in friends:
	print 'Happy New Year:', friend
print 'Done'



n = 5
while n > 0:
	print n
	n = n-1
print 'Blastoff'





def x(a):
	if a == 0.9:
		grade = 'A'
	elif a == 0.8:
		grade = 'B'
	else:
		grade = 'F'
	return grade




print x(0.9)
print x(0.5)


def addtwo(a, b):
	added = a + b
	return added
print addtwo(3, 5)

def fred():
	print "Zap"

def jane():
	print "ABC"
jane()
fred()
jane()

def computepay(hour, rate):
	Pay = (hour) * rate
	return Pay

print computepay (45, 10)

def computegrade (score):
	if score >1.0:
		return 'Invalid score'
	elif score > 0.9:
		grade = 'A'
	elif score > 0.8:
		grade = 'B'
	elif score > 0.7:
		grade = 'C'
	elif score > 0.6:
		grade = 'D'
	elif score <= 0.6:
		grade = 'F'
	return grade
print computegrade(0.6)
print computegrade(0.95)