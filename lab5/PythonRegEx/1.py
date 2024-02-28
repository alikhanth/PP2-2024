import re

word = "aaabaaaabbbaababababbaabbbb" 

print(re.findall("ab*", word))