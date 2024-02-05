def solve(head, leg):
    chikens = ((4 * head)-leg) / 2
    rabits = head - chikens
    return f"Rabits: {int(rabits)}\nChikens: {int(chikens)}" 
head = 35 
leg = 94 
print(solve(35,94))