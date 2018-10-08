import numpy as np			#Numpy Library


def main():					#defines main function

	i = 0					#declares i as an integer
	x = 119.0				#declares float x
	
	for i in range(120):	#loop i from 0 to 119, inclusive
		if((i%2)==0):		#if i is even
			x += 3.				#add 3 to x
		else:				#if i is odd
			x -= 5.				#subtract 5 from x
			
	s = "%3.2e" % x			#makes a string containing x
							#w/ scientific notation w/ 2 decimal places
		
	print(s)				#prints s to screen
		
		
	if __name__ == "__main__":		#runs the main function if it exists
		main()