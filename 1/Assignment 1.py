import turtle

wm = turtle.Screen() #does some stuff
wm.title('GUI Window') #sets GUI window name
wm.bgcolor('steelblue') #sets background color

jamie = turtle.Turtle()

#reads the first line of the file and assigns xc,yc
xc,yc =  eval(input(1))
r = eval(input(2))
x1,y1 = eval(input(3))



#sets the position of the xc yc line from (0,0)
jamie.setpos(xc,yc)
# turtle.setpos(400,300)


print(xc)
print(yc)
print(r)
print(x1)
print(y1)
# sL = 60
# basic rectangle
# jamie.fd(sL)
# jamie.lt(90)
# jamie.fd(2*sL)
# jamie.lt(90)
# jamie.fd(sL)
# jamie.lt(90)
# jamie.fd(2*sL)
# jamie.lt(90)

wm.mainloop()
