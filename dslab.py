`# from set import Set
def manipulate_data(a, b):
	if a  is "list":
		return b[::-1]
	elif a is "set":
		b = b  | {"HI", "TIA" ,"ANDELA"}
		return b;
	else:
		return b.keys()


#print manipulate_data("list", [1,2,3])
example = set(['hi'])
print manipulate_data("set", example)

print manipulate_data('dictionary',{"apples": 23, "oranges": 15})
