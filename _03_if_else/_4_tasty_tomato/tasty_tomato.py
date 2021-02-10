from tkinter import simpledialog, messagebox, Tk, Canvas

windowWidth = 600
windowHeight = 600

root = Tk()

canvas = Canvas(root, width=windowWidth, height=windowHeight, bg="#DDDDDD")
canvas.grid()

#1. Ask the user what color tomato they would like and save their response   
#   You can give them up to three choices
color = simpledialog.askstring(title="Question", prompt="What color tomato would you like? (red, orange, or yellow ")


#2. use if-else statements to draw the tomato in the color that they chose
#   you can modify the code below or draw your own tomato
canvas.create_oval(75, 200, 400, 450, fill=color, outline="")
canvas.create_oval(200, 200, 525, 450, fill=color, outline="")


canvas.create_rectangle(275, 150, 325, 230, fill="green", outline="")
canvas.create_oval(100, 150, 380, 200, fill="green", outline="")
canvas.create_oval(300, 150, 505, 200, fill="green", outline="")
    




root.mainloop()
