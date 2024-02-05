class Primes():
    def isPrime(self, num):
        if (num < 2):
            return False
        else:
            for i in range(2, num):
                if(num % i == 0):
                    return False
        return True   
    def filter_primes(self, listofnums):
        return filter(lambda x : self.isPrime(x), listofnums)
prime_filter = Primes() 
nums = [1, 8, 7, 11, 5, 17, 7, 8, 10, 9]
prime_numbers = list(prime_filter.filter_primes(nums))
print(prime_numbers)