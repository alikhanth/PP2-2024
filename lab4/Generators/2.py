def gen_even(n): 
    for i in range(0,n+1): 
        if(i%2==0): 
            yield i 
n = int(input())
evens = list(gen_even(n)) 

print(', '.join(map(str,evens)))