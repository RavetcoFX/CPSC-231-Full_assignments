import sys

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
        print(data)
        n = 0
        q = 1
        v = 2
        b = 3
        print('There are: %i cars in this puzzle\n' %len(data))
        for c in range(count-1):
            car_orientation = data[c][n]
            car_size = data[c][q]
            car_x = data[c][v]
            car_y = data[c][b]
            print ('\ncar info is:\norientation %s \ncar number %i \ncar x pos: %i \ncar y pos: %i' %(car_orientation, int(car_size),int(car_x), int(car_y)))
        
    elif len (sys.argv) != 2:
        print("error plz try again")
        sys.exit()

File_input()