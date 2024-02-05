from itertools import permutations

def print_permutations(input_string):
    perms = permutations(input_string)
    for perm in perms:
        for char in perm:
            print(char, end='')
        print()
user = str(input())
print_permutations(user)
