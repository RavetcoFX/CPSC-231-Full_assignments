class Hat_setup:
     
    def How_Many_Hats(name, Amount_of_Nuts):
        name.Hats = []
        for i in range (Amount_of_Nuts):
            name.Hats += [[3,3,3]]
        return name.Hats
    def Hats(name, Named_Hats):
        Hats = Named_Hats
        return Hats






def trainig():
    Kyle = Hat_setup()    
    print(Kyle.How_Many_Hats(45))
    return Kyle




class AI:
    def setting_Up_AI_Hats(name):
        Amount_of_Nuts = 100
        One = Hat_setup()
        Hats = One.How_Many_Hats(Amount_of_Nuts)
        return Hats
    

    #def Keeping_Track_of_Moves(name, Amount_of_Nuts, Picked_Value, Hats):
    #    Moves_Made = []
    #    Moves_Made += [[(Amount_of_nuts -1), move]]
    #    print(Moves_Made)
    #    return Picked_Value #returns the selection made from probability selection
    #    
    #def Probability_Selection(name,Current_Nuts_Hat,Hats,Amount_of_Nuts):
    #    """Function for selecting which value to go with based on the probability distribution"""
    #    # Current_Nuts_Hat is the Hats Value of the current Nut; by default this is [1,1,1]
    #    Total_Hat = (Current_Nuts_Hat[0] + Current_Nuts_Hat[1] + Current_Nuts_Hat[2])
    #    print(Total_Hat)
    #    r_int = random.randint(1, Total_Hat)
    #    Picked_Value = [1,2,3]
    #    if (r_int <= Current_Nuts_Hat[0]):
    #        move = 0
    #    elif (r_int <= Current_Nuts_Hat[0] + Current_Nuts_Hat[1]):
    #        move = 1
    #    else:
    #        move = 2        
    #    return Picked_Value[move]
    #
    def Decrement_Hats(name,Current_Nuts_Hat, move, Amount_of_nuts, Hats = 0, Win = False):
        """Function that decrements the value selected of the Hat until the game has been won or lost"""    
    
        if Win ==False:
            if Current_Nuts_Hat[move] > 0:
                print('old hats\n', Kyle.Hats)
                Hats[-2][2] = (Hats[-2][2] -1)
                print('\n New hats', Kyle.Hats)
            else:
                return Hats
            
        #for i in range(len(Moves_Made)):
        #    if Win == False:
        #        pass
        #    if Win == True:
        #        (j,k) = Moves_Made[i]
        #        Hats[j][k] += 2
        #        print('\nNew Hats')
        #        print(Hats)
        #    return Hats
    
    def AI_Turn(name, Hats, Amount_of_Nuts, Win, Turn_Number,Players, Seen = 1):
        """Defines all that should happen during an AI Turn"""
        #Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players)
        if Win == False: #Player one will be invalidated because of the while loop but in between the turns, the win variable dosen't get checked unless this if statement is present
            if Seen == 0:                
                AI_Move = 1 #Keeping_Track_of_Moves(Amount_of_Nuts,(Probability_Selection(Hats[Amount_of_Nuts-1],Hats,Amount_of_Nuts)))
                if AI_Move == 1:
                    move = 0
                if AI_Move ==2:
                    move = 1
                if AI_Move ==3:
                    move = 2
                Decrement_Hats(Hats[Amount_of_Nuts-1], move, Amount_of_Nuts, Hats)
                Amount_of_Nuts = Amount_of_Nuts - AI_Move
            if Seen == 1:
                AI_Move = 1 #Keeping_Track_of_Moves(Amount_of_Nuts,(Probability_Selection(Hats[Amount_of_Nuts-1],Hats,Amount_of_Nuts)))
                print("\nAI's Turn; How many Nuts do you take (1-3)?: %d" %(AI_Move))
                Amount_of_Nuts = Amount_of_Nuts - AI_Move
                print("Amount of Nuts remaining %d" %(Amount_of_Nuts))
        return Amount_of_Nuts


One = AI()

One.AI_Turn((One.setting_Up_AI_Hats()),100, False, 1,1)