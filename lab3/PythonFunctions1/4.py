import math
def IsPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def FilterPrime(numbers):
    return list(filter(IsPrime, numbers))
numbers_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
prime_numbers = FilterPrime(numbers_list)
print(prime_numbers)
