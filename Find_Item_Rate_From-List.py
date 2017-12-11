item_catalog = {"cables": "19", "USB": "25", "desktop": "98"}
for x in (item_catalog):
	print (x)


def key_exists (A,name):
	result = False
	for x in A:
		if x == name:
			result = True
	return result

exit_var = False
while exit_var == False:
	in_var = input ("Enter a product (or press x to quit): ")
	if key_exists(item_catalog, in_var):
		print ("Price of item is: ")
		print (item_catalog[in_var])
	if key_exists(item_catalog, in_var) == False and in_var != "x":
		print ("value does not exist")
	
	if in_var == "x":
		exit_var = True
		
	