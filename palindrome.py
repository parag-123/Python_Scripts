def if_palindrome (string):
	#reversed = string[::-1] # reverse the string and put it in reversed variable
	
# other method to reverse the string
	lst = []
	count = 1
	for i in range(0,len(string)):

		lst.append(string[len(string)-count])
		count += 1
	lst = ''.join(lst)
	
	if lst == string:
		print ("Given string is palindrome")
	else:
		print ("Given string is not palindrome" )

if_palindrome (input("Enter the string"))