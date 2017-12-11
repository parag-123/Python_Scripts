# Code to write in a new file
# with open ('D:\\Project\\parag Personal\\Python\\Files\\New_name.txt', 'rt') as f:
	# for line in f:
		# f.write (line.replace('hi there', 'hi parag'))
		
----------------------------------------------------------------------------------------------
# #Code to copy & past to another text file
# #collecting the filename we are about to copy the content

# sourcefile = input("provide the source filename:")

# #here we are opening the file we specified earlier

# txt_file = open(sourcefile)
# #here we are reading the content from the source file and storing the content

# source_content = txt_file.read()

# #providing name for the file to be created

# destinationfile = input("provide the new destination file name:")

# #here we are opening the newly created file in write mode

# target = open (destinationfile, 'w') ## a will append, w will over-write 

# #here we are writing the source file content to destination file

# target.write(source_content)

# #providing information that the task is completed

# print ("we have added those text to the file")

# target.close()
------------------------------------------------------------------------------------------
# Search & replace string in text file

import fileinput

for line in fileinput.input(D:\\Project\\parag Personal\\Python\\Files\\Text_01, inplace = True):
	print (line.replace(hello, hi), end='')