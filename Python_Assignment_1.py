# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:13:22 2016

@author: paragmehta
"""
# ---------------Question 1 --------------------------------------------------------------
def is_palindrome(x):
    x_len = len(x) # checks length of input string
    
    j = x_len -1 # as count starts from 0
    flag = 0 #Setting flag for referance
    # iterating to half of the length of string
    for i in range (0,j/2): 
        if x[i] == x[j]:
            j= j-1
        else:
            flag = 1
            break
        
    if flag == 0:
        print ("True")
    else:
        print ("False")

is_palindrome("radar")

# ---------------Question 2 --------------------------------------------------------------
for beer in range(99, 0, -1):
   if beer > 1:
      print beer, "bottles of beer on the wall,", beer, "bottles of beer."
      if beer > 2:
         wall = str(beer - 1) + " bottles of beer on the wall."
      else:
         wall = "1 bottle of beer on the wall."
   elif beer == 1:
      print "1 bottle of beer on the wall, 1 bottle of beer."
      wall = "no more beer on the wall!"
   print "Take one down, pass it around,", wall
   print "--"

# --------------- Question 3 --------------------------------------------------------------

word = "aegis"    
d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
    'g':'golf', 'h':'hotel', 'i':'India', 'j':'juliett', 'k':'kilo', 'l':'lima',
    'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
    'x':'x-ray', 'y':'yankee', 'z':'zulu'}
    
    # iterating each character of word and getting its valur from dict
for char in word:
    print (" ".join ([char,"for",d.get(char)]))
        
        
# ---------------Question 4 --------------------------------------------------------------

def alpha(x):
    words = x.split(" ") #Getting each word
    result = [] #Empty List for storage
    for item in words:
        if item not in result:
            result.append(item)
    return " ".join(sorted(result))
    
alpha("hello world and practice makes perfect and hello world again")

# ---------------Question 5 --------------------------------------------------------------
def translate (x):
    char = list(x)
# List of consonants
    consonants = list('bcdfghjklmnpqrstvwxz')
    for l in char:
        if l in consonants:
            char[char.index(l)] = l + 'o' + l # For each consonants doubling it and insrting o in between
        else:
            char[char.index(l)] = l 

            
    print ''.join(char)

translate ("this is fun")

# ---------------Question 6 --------------------------------------------------------------

def encrypt(string):
    
    # Generating list of lower and upper case letters
    LOWER_LETTERS = [chr(x) for x in range(97, 123)];
    UPPER_LETTERS = [chr(x) for x in range(65, 91)];
    
    
    rot = [] # Empty List
    #Checking for each character is lower, upper and appending to empty list
    for char in string:
        if char.islower():
            result = (LOWER_LETTERS.index(char)) + 13
            if result > 25: # if more than 25, subtracting from total char
                result = result - 26
                
            rot.append(LOWER_LETTERS[result])
            
        if char.isupper():
            result = (UPPER_LETTERS.index(char)) + 13
            if result > 25:
                result = result - 26
            rot.append(UPPER_LETTERS[result])
            
        if char not in LOWER_LETTERS + UPPER_LETTERS:
            rot.append(char)
        
    return ''.join(rot)

def decrypt(string):
    
    LOWER_LETTERS = [chr(x) for x in range(97, 123)]
    UPPER_LETTERS = [chr(x) for x in range(65, 91)]
    
    rot = []
    for char in string:
        if char.islower():
            result = (LOWER_LETTERS.index(char)) - 13
            rot.append(LOWER_LETTERS[result])
            
        if char.isupper():
            result = (UPPER_LETTERS.index(char)) - 13
            rot.append(UPPER_LETTERS[result])
            
        if char not in LOWER_LETTERS + UPPER_LETTERS:
            rot.append(char)
        
    return ''.join(rot)
        
encrypt("Caesar cipher? I much prefer Caesar salad!")   
decrypt ("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")    


#---------------Question 7 --------------------------------------------------------------

import random

attempts = 5
secret_number = random.randint(1, 100)

for attempt in range(attempts):
    guess = int(input('Take a guess: '))

    if guess < secret_number:
        print('Higher...')
    elif guess > secret_number:
        print('Lower...')
    else:
        print()
        print('You guessed it! The number was ', secret_number)
        print('You guessed it in', attempts, 'attempts')

        break

if guess != secret_number:
    print()
    print('Sorry you reached the maximum number of tries')
    print('The secret number was', secret_number)



# ---------------Question 8 --------------------------------------------------------------

def password(string):
    # Using Regex
    import re
    s = string.split(",")
    
    #Checks for condition and breaks if does not satisfy for each char in string
    for p in s:
        if (len(p)<6 or len(p)>12):  
                break  
        elif not re.search("[a-z]",p):  
                break  
        elif not re.search("[0-9]",p):  
                break  
        elif not re.search("[A-Z]",p):  
                break  
        elif not re.search("[$#@]",p):  
                break  
        elif re.search("\s",p):  
                break  
        else:
            print p

password("ABd1234@1,a F1#,2w3E*,2We3345")


      
    
            
        
 
            
            
        