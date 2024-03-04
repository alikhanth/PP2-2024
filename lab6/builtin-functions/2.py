def Count(string): 
    upper = sum(letter.isupper() for letter in string) 
    lower = sum(letter.islower() for letter in string) 
    return upper , lower 

string = str(input()) 
print(Count(string)) 