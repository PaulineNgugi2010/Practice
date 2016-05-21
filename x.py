def manipulate_data(first_parameter, second_parameter):
	if first_parameter == "list":
		return second_parameter[::-1]
	elif first_parameter == "set":
		second_parameter =  second_parameter | {"ANDELA", "TIA", "AFRICA"}
		return second_parameter
	else:
		if first_parameter == "dict":
			return second_parameter.keys()
print manipulate_data("list", [5, 6, 7, 8])
c = (set(["a", "b"])
print manipulate_data()

