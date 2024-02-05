def spy_game(nums):
    position = 0
    for num in nums:
        if position == 0 and num == 0:
            position = 1
        elif position == 1 and num == 0:
            position = 2
        elif position == 2 and num == 7:
            return True
    return False
result = spy_game([1, 0, 2, 4, 0, 5, 7]) 
print(result)
