import numpy as np

#Integers

i = 10			#integer
print(type(i))	#prints out the data type of 1

a_i = np.zeros(i,dtype=int)		#declares an array of integers
print(type(a_i))				#returns ndarray
print(type(a_i[0]))				#returns int64

#Floats

x = 119.0		#floating point number
print(type(x))	#prints data type of x

y = 1.19e2		#float 119 in sci not
print(type(y))	#prints data type of y

z = np.zeros(i,dtype=float)		#declares array of floats
print(type(z))					#returns ndarray
print(type(z[0]))				#returns float64