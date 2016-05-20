'''class Employee:
	empccount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empccount += 1

	def displaycount(self):
		print "Total Employee %d" % Employee.empccount
	def displayEmployee(self):
		print "Name: ", self.name, ", Salary: ", self.salary


emp1 = Employee('James', 35,000)
emp2 = Employee('Pauline', 500,000)
emp2.displayEmployee()
emp1.displayEmployee()
print "Total Employee %d" % Employee.empccount'''


class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name, "destroyed"
pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)

del pt1
del pt2
del pt3

class Pauline:
	paulineattr = 26
	def __init__(self):
		print "Calling Parent Constructor"
	def paulineMethod(self):
		print "Calling Method"
	def setatt(self, attr):
		def getattr(self):
			print "Parent attribute:", Pauline.paulineattr
class Blake(Pauline):
	def __init__(self):
		print 'Calling child method'
	def BlakeMethod(self):
		print "Calling child Method"

c= Blake()
c.BlakeMethod()
c.paulineMethod()
c.setatt(200)
c.getattr()



