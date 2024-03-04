def Multiply(list): 
    result = 1 
    for x in list: 
        result*=x 
    return result 

list = [1,2,3,4,5] 
print(Multiply(list)) 

#alternative
import math
list1 = [2,5,8,3] 
 
result1 = math.prod(list1)
print(result1)
