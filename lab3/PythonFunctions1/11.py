def palindrome(string):
    s = string[::-1]
    if(s == string):
        return True
    return False 
string = str(input()) 
print(palindrome(string))