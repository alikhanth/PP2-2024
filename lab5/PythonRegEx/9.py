import re 

string = "HelloMyNameIsAlikhan"  

result = re.findall("[A-Z][a-z]*", string)
print(' '.join(result))