def squ_gen(N):
    for i in range(1,N+1):
        yield i ** 2

N = int(input())
squares = squ_gen(N)

for num in squares:
    print(num)
