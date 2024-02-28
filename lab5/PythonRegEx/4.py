import re

word = "Write a Python program to Find the SequEnces of One upPer case LeTter followed by lower Case letters." 

print(re.findall("[A-Z][a-z]+",word)) 
 
