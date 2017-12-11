def sum_of_numbers (x):
	total = 0
	for y in x:
		total += y
	return total

# take user input & convert it to list using eval function
lst = input ("Enter your list")
lst = eval(lst)

print ("sum of numbers is: ", sum_of_numbers(lst))