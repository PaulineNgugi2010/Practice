'''def printinfo(arg1, *varuple):
	print "Output is:" , arg1
	for var in varuple:
		return "Var is", var
	return


printinfo(10)
printinfo(50, 60, 70)
'''



money = 2000
def addmoney():
	global money
	money = money + 1
print money
addmoney()
print money