#Note that the program has to be fed a .dat file from the command line to run i.e C:\User>python3 < sample1.dat

import turtle #brings in digital etch-a-sketch Library; this is the GUI library that will draw the circle and lines, aswell as the intersects
import math #brings in the math library; The program needs this to do the square root calcualtions

qq = turtle.Screen() #makes it so I don't have to type out turtle.screen() constantly
qq.title('Kieran Wood Assignment 1') #sets GUI window name

#fixes the issue where the image is drawn off screen
qq.setworldcoordinates(-200,-150,1000,800)

#assigning values for all required variables to do the calculations from the .dat file:

#These values define the coordinates for the center of the circle; The values are also used in the intersection calculations
xc, yc = eval(input())

#this is the value used for the radius of the circle being drawn; also used in the intersection calculations
r = eval(input())

#these are the variables used to draw the intersecting line and are also used in the intersection calculations
x1, y1 = eval(input())
x2,y2 = eval(input())


#math to define the variables that will be used to give the intercepts
a = ((x2-x1)**2)+((y2-y1)**2)
b = (2*((x1-xc)*(x2-x1)+(y1-yc)*(y2-y1)))
c = ((x1-xc)**2)+((y1-yc)**2)-(r**2)


#defining all my functions
def run_to_middle(cc):
    """sets the position of jamie to the xc yc positions and moves it down one radius so that the circle is being drawn with xc, yc as the center from (0,0)"""
    cc.up()
    cc.setpos(xc,yc)
    cc.lt(270)
    cc.fd(r)
    cc.lt(90)
    cc.down()
def Circlepoint(q):
    """function for circling the location of the interceptsl; the q value is the return value from intersect_calc_pos() and,or intersect_calc_neg()"""
    jamie.up()
    if q==None:
        pass
    else:
        jamie.setpos(q)
        jamie.lt(-90)
        jamie.fd(15)
        jamie.lt(90)
        jamie.down()
        jamie.circle(15)
        jamie.up()
def drawline(bb):
    bb.up()
    bb.setpos(x1,y1)
    bb.down()
    bb.setpos(x2,y2)
def intersect_calc_pos():
    """Function to determine the intersection points of the line and the circle: this one does b Plus the square root of b squared minus 4ac all divided by 2a"""
    if (((b**2)-4*a*c)) < 0:
        return None
        pass

    if (((b**2)-4*a*c)) >= 0:
        alpPos=((-b+math.sqrt(((b**2)-4*a*c)))/(2*a))
        #print(alpPos)
        if 1<alpPos or alpPos<0:
            return None
        else:
            xpos = ((1-alpPos)*x1+(alpPos*x2))
            ypos = ((1-alpPos)*y1+(alpPos*y2))
            return (xpos,ypos)
def intersect_calc_neg():
    """Function to determine the intersection points of the line and the circle:this one does b minus the square root of b squared minus 4ac all divided by 2a"""
    if (((b**2)-4*a*c)) < 0:
        return None
        pass

    if (((b**2)-4*a*c)) >= 0:
        alpNeg=((-b-math.sqrt(((b**2)-4*a*c)))/(2*a))
        #print(alpNeg)
        if 1<alpNeg or alpNeg<0:
           return None
        else:
            yneg = ((1-alpNeg)*y1+(alpNeg*y2))
            xneg = ((1-alpNeg)*x1+(alpNeg*x2))
            return (xneg,yneg)

#assigns a turtle the name jamie; it will execute all the functions 
jamie = turtle.Turtle()

#speeds Jamie up so that it dosen't take so long to run each time
jamie.speed(5)

#uses the run to middle funciton; moves jamie to (xc,yx) and then moves jamie down r distance so that (xc,yc) is the center of the circle and not the bottom 
run_to_middle(jamie)

#draws a circle with a radius of r
jamie.circle(r)

#calls the drawline function; draws a line from (x1,y1) to (x2,y2)
drawline(jamie)

#runs the circling function with whatever values return from the intersect calculation; The two functions correspond to subtracting and adding the b value before the square root respectively
#if there are no intersections along the line it does nothing
Circlepoint(intersect_calc_neg())
Circlepoint(intersect_calc_pos())

#The mainloop that keeps the window open
qq.mainloop()