import re

string = "HelloMyNameIsAlikhan" 

print(re.findall(r'[A-Z][^A-Z]*',string))
