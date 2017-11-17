

Kyle_Carnumber=1

Goal_Car=0



#Game Class
def Update_Grid(Goal_Car, Blockers):
    """Creates the initial grid that the user will play from; needs to call place cars"""
    verticle = 6
    Horizontal = 6
    count = 0
    Container_List = []
    for i in range(0,verticle):#creates the verticle spacing using the horizontal elements created within the for loop
        goal_car_row = 2
        goal_car_collum = 2
        
        count += 1 
        Empty_Value = [' █ '] #The Value for empty space
        Container_List.append(Empty_Value*Horizontal) #Creates the horizontal elements of the grid
        Container_List.append(' ')
        #Container_List.append(str(i))
    Container_List[goal_car_row-1][goal_car_collum-1] = 1
    print (Container_List)
    print("\n Grid version\n")
    return Container_List


def Print_Grid(Grid):
    for j in (Grid):
        print (" ".join(j))



def Turn(Car, Row, Collum):
    """The function that will define taking the turn"""
    #move car to the row location
    #move car to collum location
    pass
def Place_cars(Car, Row , Collum):
    """Will need to be able to place the cars in their initial locations reading from the file provided"""
    pass


Print_Grid(Update_Grid(None,None))