# take input from user for 3 numbers
# comapre number 1 with other 2 numbers- 
# comapre number 2 with other 2 numbers
# comapre number 3 with other 2 numbers

# Take 3 input number from user
# num1 = int(input ("Enter one number: "))
# num2 = int(input ("Enter second number: "))
# num3 = int(input ("Enter third number: "))

# # compare each number with other the decide on greatest number
# if (num1 > num2 and num1 > num3):
	# print ("the largest number is", num1)
# elif (num2 > num1 and num2 > num3):
	# print ("the largest number is", num2)
# else:
	# print ("the largest number is", num3)
		

		
def max_of_three (x,y,z):
	# x = int(input ("Enter one number: "))
	# y = int(input ("Enter second number: "))
	# z = int(input ("Enter third number: "))

	if (x > y and x > z):
		return x
	elif (y > x and y > z):
		return y
	else:
		return z


print ("Larget number of all is ", max_of_three (x=int(input ("Enter one number: ")),y = int(input ("Enter second number: ")),z= int(input ("Enter third number: "))))


