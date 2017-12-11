def factorial (num):
	x = 1
# check if the number is not negative or c. 
	if num < 0:
		print ("Please enter valid number")

	elif num == 0:
		print ("Factorial of 0 is 1")
	
	else:
		for i in range (1, num+1):
			x = x*i
			return x

num = int( input ("Enter number to get factorial: "))
print (factorial (num))
		
