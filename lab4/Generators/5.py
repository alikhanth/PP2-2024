def gen_decreasing(n): 
    while n>=0: 
        yield n 
        n-=1 
n = int(input()) 
for num in gen_decreasing(n): 
    print(num)