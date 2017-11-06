
Hats = []
for i in range (45):
    Hats += [[3,3,3]]

Moves_Made = []

Current_Nut = 42
move = 2
Hats[Current_Nut][move] -= 1 

Moves_Made += [[Current_Nut, move]]
print("\nHats")
print(Hats)

for i in range(len(Moves_Made)):
    (j,k) =Moves_Made[i]
    print('j')
    print (j)
    print('\nk')
    print(k)
    Hats[j][k] += 2
    print('\nNew Hats')
    print(Hats)
