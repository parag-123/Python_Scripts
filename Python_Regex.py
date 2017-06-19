# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:49:26 2017

@author: Parag.Mehta
"""
# Importing Regex module
import re
# input message from where Email/Date/Time to be extracted
message = "Sachin.r.t.73@yahoo.com where i am at 2016.10.16 and 13th November 2012 and 15 October at 10:30 pm"
# Regex to filter Email
reg_email = re.findall(r'([\w\.]+@[\w+\.]+)',message)
#Regex to filter numeric Date
reg_date = re.findall(r'([0-9]{2,4}\-?\.?[0-9]{2}\-?\.?[0-9]{2,4})', message)
# Regex to filter date in words & numbers
reg_date1 = re.finditer(r'(\d+\w+\s+?(January|February|March|April|May|June|July|August|September|October|November|December)(\s\d{4})?)', message)
#regex to filter time
reg_time = re.finditer(r'(((\d{1,2}\s?)(:{1})?(\d{1,2}\s:)?(:{1})?(\d{1,2}\s))?(am|pm)?)$',message)

#Print commands
print ("email IDS: " + str(reg_email))
print ("Dates & times: " + str(reg_date))
for m in reg_date1:
    print (m.group())
for i in reg_time:
    print (i.group())




