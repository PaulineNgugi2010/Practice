'''file_name = raw_input("Enter file_name: ")
if len(file_name) ==0:
	print "Next time enter something"
	sys.exit()
try:
	file_name = open(file_name, "r")
except IOError:
	print "There was an error reading file"
	sys.exit()
file_text = file.read()
file.close()
print file_text

list = ['pauline', 1, 3, 'John']
tuple = ('heroku', 14, 17, 'damaris')

list[3] = 2000
print list

tinydict = {'name:' 'Pauline', 'Age:', 26, 'Religion:', 'Christian'}
print tinydict
'''

items = [1, 2, 4, 4, 5 ,6, 7]
items2 = [45,67,86]

#print cmp(items, items2)
#print max(items2)

'''def maxno(num1):

	max1 = None

	for i in num1:
		if i > max1: max1 = i
	return i

print maxno([3, 4, 5, 90])




#print max(items)
'''


def reverse1(item):
	for i in range(len(item) - 1, -1, -1):
		print item[i]

# print items [::-1] 
# del items[1:2];

# print items

reverse1([1, 2, 3, 4, 78, 45])



