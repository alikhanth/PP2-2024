def is_palindrome (string): 
    reversed_word = ''.join(reversed(string)) 
    if string == reversed_word: 
        return True 
    else: 
        return False 

string = str(input()) 
if is_palindrome(string): 
    print(f"{string} is palindrome") 
else: 
    print(f"{string} is not palindrome")