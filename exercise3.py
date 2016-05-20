'''def maxno(num1):

	max1 = 0
	x =[]

	for i in num1:
		if i > max1: 
			max1 = i
	return max1 

#print maxno([4, 5, 90, 4])



tuple1= (['pauline', 3, 'grace'], 'Kamara', 'Heidi', 6)
print 'tuple1 :',  tuple1

print len(tuple1)
'''

import time;
import calender

ticks = time.time()
print "Number of ticks since 12:00am, Dec 7, 1989:", ticks

localtime = time.localtime(time.time())
print "Local current time:", localtime


cal = calender.month(1989, 12)
print "Calende is: ", cal