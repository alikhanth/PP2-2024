import re

word = "aaabaaaabbbaababababbaabbbb" 

print(re.findall("ab{2,3}",word))