
class cars:
    
    def __init__(self):
        self.kyle = [[1]]
        self.jamie = [[2]]
        Init_Grid()
    def Init_Grid(self):
        """Creates the initial grid that the user will play from; needs to call place cars"""
        verticle = 6
        Horizontal = 6
        for i in range(verticle):#creates the verticle spacing using the horizontal elements created within the for loop
            Container_List = []
            Base_Value = [[1]]
            Container_List += ((self.kyle+self.jamie)*Horizontal) #Creates the horizontal elements of the grid
            print(Container_List)


cars