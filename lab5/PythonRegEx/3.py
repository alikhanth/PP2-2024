import re

word = "Write_a_Python_program_to_find_sequences_of_lowercase_letters_joined_with_a_underscore." 

print(re.findall("[a-z]+_[a-z]+",word)) 
 
#print(re.findall("[a-z]{1}_[a-z]{1}",word))