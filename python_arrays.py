#define an array
x = [0.0, 3.0, 5.0, 2.5, 3.7]
print(type(x))

x.pop(2)				#removes the third element of array
print(x)

x.remove(2.5)			#removes elements equal to 2.5
print(x)

x.append(1.2)			#adds element to end of array
print(x)

y = x.copy()			#copies array as y
print(y)

print(y.count(0.0))		#counts how many elements are 0.0 

print(y.index(3.7))		#prints the index with value 3.7

y.sort()				#sorts array smallest to largest
print(y)

y.reverse()				#sorts largest to smallest
print(y)

y.clear()				#removes all elements in y
print(y)