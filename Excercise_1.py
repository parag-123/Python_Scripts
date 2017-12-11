total = 0
count = 0
list = list()
while True:
	user_input = input ("Enter a number: " )
	try:
		abc = int(user_input)
	except:
		if user_input == 'done':
			average = total / count
			print (" total: ", total, "Count: ", count, "Average: ", average, "Max: ", maximum, "Min: ", minimum )
			break
		else:
			print ('bad input')
	list.append(abc)
	minimum = min(list)
	maximum = max(list)
	
	total = total + abc
	count = count +1
	
	
