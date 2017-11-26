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
        #self.carsize = eval(input("what is the carsize?:"))
        self.carsize = 2
         

    def get_carsize(self):
       return self.carsize
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
    #car_value = 6 # needs to be equal to the length of the lines of the text file
    car_dict = {}
    car_value = []
         
    for i in range(1,(car_value+1)):#Creates the right amount of instances based on line numbers in text file
        car_dict['car_%i' %(i)] = Cars()

    print(car_dict['car_1'].carnumber)
    def Startup():
        Game.File_input() 
        Game.Game_loop() 

    def Game_loop():
        """What will keep the game running until it is over"""
        Gui_ver = False
        if Gui_ver == False:
            Game.Update_Grid()
            while (Gui_ver == False and Game.Game_over() ==False):
                Game.Turn()
            

    def Turn():
        """The function that will define taking the turn"""
        [number, row_x, collumn_y] = eval(input("Please select a Car Number, The Row you would like to move the car to, and the Collumn  you would like to move the car to:"))
        current_car = Game.car_dict['car_%i' %(number)]
        print("car selected's orientation is: %s \n" %(current_car.get_orientation()))
        print("car selected's size is: %s \n" %(current_car.get_carsize()))
        current_car.set_y(collumn_y)
        current_car.set_x(row_x)
        print("Car #%i new positon is: X=%i Y=%i" %(number, current_car.get_x(), current_car.get_y()))
        Game.Update_Grid(number)

    def Update_Grid(car_num = None):
        """Creates the initial grid that the user will play from; needs to call place cars"""
        vertical = 6
        horizontal = 6
        Container_List = []
        Game_over = Game.Game_over()
        if car_num ==None:
            for i in range(0,vertical):#creates the verticle spacing using the horizontal elements created within the for loop
                Empty_Value = [0] #The Value for empty space
                Container_List.append(Empty_Value*horizontal) #Creates the horizontal elements of the grid
                print (Container_List)
                print("\n Grid version\n")
                return Container_List

        if (Game_over ==False and car_num!=None):

            current_car = Game.car_dict['car_%i' %(car_num)]
            Cars_Orientation = current_car.get_orientation()
            print(current_car.carnumber)
            for i in range(0,vertical):#creates the verticle spacing using the horizontal elements created within the for loop
                Car_row = current_car.get_x() - 1
                Car_collum = current_car.get_y() - 1
                Car_orientation = current_car.get_orientation()
                Empty_Value = [0] #The Value for empty space
                Container_List.append(Empty_Value*horizontal) #Creates the horizontal elements of the grid
            if current_car.get_carsize() == 2:
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
            return Container_List
        else:
            pass
    def Game_over():
        Goal_car = Game.car_dict['car_1']
        if (Goal_car.get_pos() == (2,6)):
            print("\nwould you look at that thats the ending all right, good job, keep up the nice work lad, you got a career ahead of you")
            return True
        else:
            return False

    def File_input():
        if len (sys.argv) == 2:
            input_file = open(sys.argv[1])
            line = input_file.readline()
            count = 1
            data = []
            while line:
                   print("Line {}: {}".format(count, line.strip()))      
                   data += [[line.strip()[0],line.strip()[3], line.strip()[6], line.strip()[9]]]
                   #data += line.strip()[3]
                   #data += line.strip()[6]
                   #data += line.strip()[9]
                   line = input_file.readline()
                   count += 1
            print("\nFull data list from file:")
            print(data)
            print('')
            n = 0 #index where the relevant information is found in the data list; used in the next for loop
            q = 1 #index where the relevant information is found in the data list; used in the next for loop
            v = 2 #index where the relevant information is found in the data list; used in the next for loop
            b = 3 #index where the relevant information is found in the data list; used in the next for loop
            print('There are: %i cars in this puzzle\n' %len(data))
            Game.Count = count
            for c in range(count-1):
                car_orientation = data[c][n]
                car_size = data[c][q]
                car_x = data[c][v]
                car_y = data[c][b]
                print ('\ncar info is:\norientation %s \ncar number %i \ncar x pos: %i \ncar y pos: %i' %(car_orientation, int(car_size),int(car_x), int(car_y)))
        return [car_orientation,car_size,car_x,car_y]
            

Game.Startup()

if len (sys.argv) != 2:
    print("error plz try again")
    sys.exit()


   