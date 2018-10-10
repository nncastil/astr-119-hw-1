#defining a dictionary data structure

example_dict = {					#key	:	value of element
	"class"			:	"Astr 119",
	"prof"			:	"Brant",
	"awesomeness"	:	10
}
print(type(example_dict))			#says "dict"

course = example_dict["class"]		#to get a value via the key above
print(course)

example_dict["awesomeness"] += 1	#to change a value in key (increases)

print(example_dict)

for x in example_dict.keys():
	print(x,example_dict[x])		#prints dictionary key and element value