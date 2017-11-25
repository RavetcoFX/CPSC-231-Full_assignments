#assignment 4 - Kieran Wood
import sys

class Cars:
    """This class contains all the attributes for each car instance"""
    carnumber = 1
    
    
    def __init__(self):
        """Constructor that sets the carnumber variable in the local namespace so that each instance has it's own number, |needs to be done|and sets the initial positions of each instance based on the file input"""
        self.carnumber = Cars.carnumber #sets instances car number to the current class global carnumber
        Cars.carnumber += 1 #after assigning the carnumber to itself it needs to increment by one to have an accurate number based on the instances
        self.x = 0 # Initially comes from source game file
        self.y = 0 # Initially comes from source game file
        self.Orientation = input("What is the orientation of carnumber %i (h or v): " %(self.carnumber)) # Initially comes from source game file

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_pos(self):
        return (self.x,self.y)
    def set_x(self, new_x):
        self.x = new_x
    
    def set_y(self, new_y):
        self.y = new_y

    def get_orientation(self):
        return self.Orientation


class Game:
    car_value = 6
    car_dict = {}
         
    for i in range(1,(car_value+1)):#Creates the right amount of instances based on line numbers in text file
        car_dict['car_%i' %(i)] = Cars()

    print(car_dict['car_1'].carnumber)
    def Game_loop():
        """What will keep the game running until it is over"""
        Gui_ver = False
        if Gui_ver == False:
            Game.Update_Grid(1)
            while (Gui_ver == False and Game.Game_over() ==False):
                Game.Turn()
            

    def Turn():
        """The function that will define taking the turn"""
        [number, row_x, collumn_y] = eval(input("Please select a Car Number, The Row you would like to move the car to, and the Collumn  you would like to move the car to:"))
        current_car = Game.car_dict['car_%i' %(number)]
        print("car selected's orientation is: %s \n" %(current_car.get_orientation()))
        current_car.set_y(collumn_y)
        current_car.set_x(row_x)
        print("Car #%i new positon is: X=%i Y=%i" %(number, current_car.get_x(), current_car.get_y()))
        Game.Update_Grid(number)

    def Update_Grid(car_num):
        """Creates the initial grid that the user will play from; needs to call place cars"""
        Game_over = Game.Game_over()
        if Game_over ==False:
            vertical = 6
            horizontal = 6

            Container_List = []
            current_car = Game.car_dict['car_%i' %(car_num)]
            Cars_Orientation = current_car.get_orientation()
            print(current_car.carnumber)
            for i in range(0,vertical):#creates the verticle spacing using the horizontal elements created within the for loop
                Car_row = current_car.get_x() - 1
                Car_collum = current_car.get_y() - 1
                Car_orientation = current_car.get_orientation()
                Empty_Value = [0] #The Value for empty space
                Container_List.append(Empty_Value*horizontal) #Creates the horizontal elements of the grid
            if 'h' == Cars_Orientation:
                if (current_car.get_y() == 1):
                    print("Please make a valid selection:\n")
                    Game.Turn()
                else:
                    Container_List[Car_row][Car_collum] = current_car.carnumber 
                    Container_List[Car_row][Car_collum-1] = current_car.carnumber 
            if 'v' == Cars_Orientation:
                #if (current_car.get_x() == 1):
                #    print("Please make a valid selection:\n")
                #    Game.Turn()
                Container_List[Car_row][Car_collum] = current_car.carnumber 
                Container_List[Car_row-1][Car_collum] = current_car.carnumber 
            
            print (Container_List)
            print("\n Grid version\n")
            return Container_List
        else:
            pass
    def Game_over():
        Goal_car = Game.car_dict['car_1']
        if (Goal_car.get_pos() == (2,5)):
            return True
        else:
            return False





if __name__ == '__main__':
    if len (sys.argv) != 2:
        Game.Game_loop()
        #sys.stderr.write()
        sys.exit()