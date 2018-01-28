# Question 1

#Getting the tuple
tup = (("Tom","19","80"), ("John","20","90"), ("Jony","17","91"), ("Jony","17","93"), ("Json","21","85"))
# This will sort the tuple based on name, age & score in priority
print (sorted(tup))

#Question 2

text =u"""DTU course 02820 is taught by Mr. Bartlomiej Wilkowski, Mr. Marcin Marek Szewczyk & Finn
 ̊Arup Nielsen, Ph.D. Some of aspects of the course are: 
     machine learning and web 2.0. The telephone to Finn is (+45) 4525 3921, 
     and his email is fn@imm.dtu.dk. A book published by O’Reilly called ’Programming Collective 
     Intelligence’ might be useful. It costs $39.99 or 285.00 kroner in Polyteknisk Boghandle. 
     Is ’Text Processing in Python’ appropriate for the course? Perhaps! 
     The constructor function in Python is called "__init__()". 
     fMRI will not be a topic of the course."""

#Splitting into sentences
import re

ending_with = re.compile(r'([\.\?\!]\s+)')
not_ending = re.compile(r'(?:Mrs?|Jr|i\.e)\.\s*$')
parts = ending_with.split(text)
sentence = []
for part in parts:
  if len(part) and len(sentence) and ending_with.match(sentence[-1]) and not not_ending.search(''.join(sentence)):
    print(''.join(sentence))
    sentence = []
  if len(part):
    sentence.append(part)
if len(sentence):
  print(''.join(sentence))

#Splitting into words
words = text.split()
print words

#Question 3:
string = 'Hello world!'
# For each letter in the string, this will return true for Upper case letter
print("Upper Case: ", sum(1 for c in string if c.isupper()))
# For each letter in the string, this will return true for lower case letter

print("Lower Case: ", sum(1 for c in string if c.islower()))