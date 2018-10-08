#String

s = "I am a string."
print(type(s))			#prints "str"

#Boolean

yes = True				#Boolean True
print(type(yes))

no = False				#Boolean False
print(type(no))

#List -- ordered and changeable

alpha_list = ["a","b","c"]		#list initialization
print(type(alpha_list))			#says "tuple"
print(type(alpha_list[0]))		#says "string"
alpha_list.append("d")			#adds d to list
print(alpha_list)				#prints list

#Tuple -- ordered and unchangeable

alpha_tuple = ("a","b","c")		#tuple initialization
print(type(alpha_tuple))		#says "tuple"

try:											
	alpha_tuple[2] = "d"						#will raise TypeError
except TypeError:
	print("We can't add elements to tuples!")	#prints this message when TypeError
print(alpha_tuple)