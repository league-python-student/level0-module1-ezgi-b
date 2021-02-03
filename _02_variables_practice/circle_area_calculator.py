import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    r = simpledialog.askinteger(title="Question", prompt="Enter a radius for a circle.")
    
    # Make a new turtle
    sheldon = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    sheldon.circle(radius=r)

    # Call the turtle .penup() method
    sheldon.penup()
    # Move your turtle to a new x,y position using .goto()
    sheldon.goto(x=0, y=-100)
    # Calculate the area of your circle and store it in a variable, you can use math.pi
    area = math.pi*r*r
    # Write the area of your circle using the turtle .write() method
    sheldon.write(arg="area = " + str(area), move=True, align='center', font=('Arial',12,'normal'))

    # Hide your turtle
    sheldon.hideturtle()
    # Call turtle.done()
    turtle.done()
    window.mainloop()