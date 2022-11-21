import turtle
import numpy as np


def main():
    # create Turtle object
    myTurtle = turtle.Turtle()
    
    # set speed to 'fastest'
    myTurtle.speed(0)
    
    # change background color
    turtle.Screen().bgcolor("grey")

    # TODO: define different colors here
    colors = ["white", "red", "green", "orange", "magenta", "blue", "black", "yellow", "pink"]


    def snowflake_branch(size):
    """ This function draws one branch of the snowflake. """
        for _ in range(3):
            for _ in range(3):
                myTurtle.forward(size/3)
                myTurtle.backward(size/3)
                myTurtle.right(45)
            myTurtle.left(90)
            myTurtle.backward(size/3)
            myTurtle.left(45)
        myTurtle.right(90)
        myTurtle.forward(size)

    for _ in range(10):
        # define some params
        size = 18
        pos = [np.random.randint(-300, 300), np.random.randint(-300, 300)]
        
        # TODO: set snowflake color here (one of the colors defined above)
        myTurtle.color(colors[np.random.randint(0, len(colors))])
        
        # Go to the start position of the snowflake
        myTurtle.penup()
        myTurtle.goto(pos[0], pos[1])
        myTurtle.pendown()
        
        # draw the snowflake
        for _ in range(8):
            snowflake_branch(size)
            myTurtle.left(45)

    input("Press Enter to continue...")


if name == __main__():
