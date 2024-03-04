import time
import math

num = int(input()) 
miliseconds = int(input()) 
seconds = miliseconds/1000 

time.sleep(seconds) 

root = math.sqrt(num)

print(f"Square root of {num} after {miliseconds} is {root}")
