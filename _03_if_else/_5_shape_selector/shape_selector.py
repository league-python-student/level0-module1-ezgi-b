import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    shelly = turtle.Turtle(shape="turtle")
    
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="Question", prompt="What shape do you want to draw?")
    
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "circle":
        shelly.circle(50)
    elif shape == "square":
        for i in range(4):
            shelly.forward(100)
            shelly.right(90)
    elif shape == "triangle":
        for i in range(3):
            shelly.forward(120)
            shelly.right(120)
    elif shape == "trapezoid":
        shelly.forward(100)
        shelly.left(120)
        shelly.forward(50)
        shelly.left(60)
        shelly.forward(50)
        shelly.left(60)
        shelly.forward(50)
        shelly.left(120)
    elif shape == "pentagon":
        for i in range(5):
            shelly.forward(80)
            shelly.right(72)
    elif shape == "hexagon":
        for i in range(6):
            shelly.forward(70)
            shelly.right(60)
    elif shape == "octagon":
        for i in range(8):
            shelly.forward(50)
            shelly.right(45)
    elif shape == "dodecagon":
        for i in range(12):
            shelly.forward(30)
            shelly.right(30)
    elif shape == "star":
        for i in range(5):
            shelly.forward(100)
            shelly.right(144)
    else:
        messagebox.showinfo(message="The turtle does not know how to draw that shape.")

    # Call the turtle .done() method
    turtle.done()
    
#    window.mainloop()
