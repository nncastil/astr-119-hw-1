#to deal with unexpected results

try:
	print(a)								#throws an exception, a is not defined
except:
	print("a is not defined!")				#displays this message instead
	
try:
	print(a)
except NameError:							#when NameError message shows up
	print("a is still not defined!")
except:
	print("Something else went wrong.")
	
print(a)			#will break the program bc a is not defined