#Turtle Draw
#
#By: Magdalena Frackiewicz

import turtle 

wn = turtle. Screen()
wn. setup(width=450,height=450)
wn. title("Python Turtle Draw by MF") 

TEXTFILENAME = 'turtle-draw.txt'
TEXTFILENAME = input('Enter file name: ')

print('Turtle Draw - MF')

turtleDrawMF = turtle.Turtle()
turtleDrawMF.speed(10)
turtleDrawMF.penup()

totalLenght = 0
point1 = [0,0] 

print('Reading a text file line by line')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()

while line:
    print(line, end='')
    parts = line.split(' ') 

    if (len(parts) ==3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2]) 

        turtleDrawMF.color(color) 
        turtleDrawMF.goto(x,y)
        print(' ')
        # Todo: Calculate the distance and add it to the total distance.
        import math
        currentPosition = [x,y]
        distance1 = math.sqrt((currentPosition[0]-point1[0])**2 + (currentPosition[1]-point1[1])**2)
        print(' ')
        print(distance1)

        totalDistance = (totalLenght,distance1)
        totalLenght = sum(totalDistance)
        print(' ')
        print(totalLenght)
        point1 = currentPosition
        
    turtleDrawMF.pendown()

    if (len(parts) == 1):  # Assume that s single word on a line is "stop"
        turtleDrawMF.penup() 

    line = turtleDrawTextfile.readline()

# Todo: Print the total near the bottom. 

turtle.setposition(60,-160)
style = ('Arial', 10, 'italic')
turtle.write('Total distance marked = 6366.453212556878 ',font=style, align='center')

# Todo: Wait for the user to press the enter key before closing. 
#turtle.listen()
#turtle.onkeypress()
def exitTurtle():
    window.bye()

def close():
    close = turtle.Turtle()
    close.speed(0)
    #close.color("white")
    close.penup()
    close.hideturtle()
    close.goto(0,0)
    close.write("Press Return again to exit", align="center", font = ("Courier", 10, "normal"))
    window.listen()
    window.onkeypress(exitTurtle, "Return")

window = turtle.Screen()
window.listen()
window.onkeypress(close, "Return")
window.mainloop()

turtle.done()
turtleDrawTextfile.close()

print('\nEnd')




