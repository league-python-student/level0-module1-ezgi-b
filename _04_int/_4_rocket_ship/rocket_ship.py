from tkinter import *

windowWidth = 800
windowHeight = 800
root = Tk()

canvas = Canvas(root, width=windowWidth, height=windowHeight, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()
    
# this code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # draws a dark blue background
    canvas.create_rectangle(0, 0, windowWidth, windowHeight, fill="#000050")
    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y
    
    # this defines the x and y coordinated of all three points
    # of a triangle
    points = [x, y, x + 50, y + 90, x - 50, y + 90]
    canvas.create_polygon(points, fill='gray', width=2) #draws triangle
    
    # 1. Add details to your rocket to make it look better. You can look at rocket.png for inspiration.
    points = [x - 50, y + 90, x + 50, y + 90, x + 50, y + 240, x - 50, y + 240]
    canvas.create_polygon(points, fill='green', width=2)
    t = 45
    z = 70
    g = 60
    l = 370
    points = [x + t, y + 240, x - t, y + 240, x - z, y + l - 50, x - g, y + l, x + g, y + l, x + z, y + l - 50]
    canvas.create_polygon(points, fill='red', width=2)
    t = 30
    z = 50
    g = 40
    l = 360
    points = [x + t, y + 240, x - t, y + 240, x - z, y + l - 50, x - g, y + l, x + g, y + l, x + z, y + l - 50]
    canvas.create_polygon(points, fill='orange', width=2)
    t = 15
    z = 40
    g = 30
    l = 350
    points = [x + t, y + 240, x - t, y + 240, x - z, y + l - 50, x - g, y + l, x + g, y + l, x + z, y + l - 50]
    canvas.create_polygon(points, fill='yellow', width=2)
    t = 5
    z = 20
    g = 10
    l = 340
    points = [x + t, y + 240, x - t, y + 240, x - z, y + l - 50, x - g, y + l, x + g, y + l, x + z, y + l - 50]
    canvas.create_polygon(points, fill='white', width=2)

    
    #2. Modify the locations of the shapes above so the rocket will be drawn where the mouse is clicked
    

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()