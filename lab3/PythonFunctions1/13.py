import random 

def GuessTheNum(): 
    guess_num = random.randint(1,20) 
    attempt = 0 
    name = input("Hello! What is your name?\n") 
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.") 
    number = None
    while (number!=guess_num):
        number = int(input("Take a guess\n"))
        attempt += 1
        if(number < guess_num):
            print("\nYour guess is too low.")
        elif(number > guess_num):
            print("\nYour guess is too big.") 
    
    
    print(f"Good job, {name}! You guessed my number in {attempt} guesses!")
     

GuessTheNum()