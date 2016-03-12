#!/usr/bin/python3

# def is used to define a function
# Syntax: 
#	def <function-name>(<param1>, <param2>, ...):
def main():
	print("Main function")
	addition(45, 45)
	addition()

# a and b are having default values
def addition(a = 5, b = 5):
	print("Addition: ", a + b)


if __name__ == "__main__": main()