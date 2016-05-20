def temp_convert(var):
	try:
		return int(var)
	except ValueError, Argument:
		print "The argument does not contain numbers\n", Argument

temp_convert("xyz")

'''def functionName(level):
	if level < 1:
		raise "Invalid level!", level
try:
	Business Logic here 
except "Invalid Level!":
	Exceptption handling here...
else:
	Rest of Code here 
	

class Networkerror("Bad hostname"):
	def __init__(self, arg):
		self.args = arg
	try:
		raise Networkerror("Bad hostname")
	except Networkerror, e:
		print e.args'''
