
Hats = []
for i in range (45):
    Hats += [[3,3,3]]

Moves_Made = []

Current_Nut = 42
move = 2
Hats[Current_Nut][move] -= 1 

Moves_Made += [[Current_Nut, move]]
print("\nHats")
#print(Hats)



Current_Nut = 39
move = 2
Hats[Current_Nut][move] -= 1 
Moves_Made += [[Current_Nut, move]]

Current_Nut = 36
move = 2
Hats[Current_Nut][move] -= 1 
Moves_Made += [[Current_Nut, move]]

Win = True

print(Moves_Made)

if Win == True:
    for i in range(len(Moves_Made)):
        (j,k) =Moves_Made[i]
        print('j')
        print (j)
        print('\nk')
        print(k)
        Hats[j][k] += 2
        print('\nNew Hats')
        print(Hats)






    #Section For decrementing Hats
    Moves_Made = []
    Moves_Made += [[(Amount_of_nuts -1), move]]
    print(Moves_Made)
    if Win ==False:
        if Current_Nuts_Hat[move] > 0:
            Current_Nuts_Hat[move] = ((Current_Nuts_Hat[move]) - 1)
        else:
            return Hats
        
    for i in range(len(Moves_Made)):
        if Win == False:
            pass
        if Win == True:
            (j,k) = Moves_Made[i]
            Hats[j][k] += 2
            print('\nNew Hats')
            print(Hats)
        
    return Hats