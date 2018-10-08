import numpy as np
import sys

def expo(x):				#defines a function that returns value
	return np.exp(x)		#returns the np e^x function
	
def show_expo(n):				#a subroutine that does not return value
	for i in range(n):
		print(expo(float(i)))	#calls the expo function
		
def main():						#defines main function
	n = 10						#default function for n
	
	if(len(sys.argv)>1):		#check for a command line argument
		n = int(sys.argv[1])	#uses argument for n if provided
		
	show_expo(n)				#calls show_expo subroutine
	
	
if __name__ == "__main__":
	main()