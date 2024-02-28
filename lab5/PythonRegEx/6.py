import re 

text = "I am writing a regex.to match any numbers, commas, dots, except when..they are at the end of the number." 

pattern = r'[ ,.]' 

retext = re.sub(pattern,':',text)
print(retext)
