# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
from tkinter import simpledialog, messagebox, Tk, Canvas
import math
if __name__ == "__main__":
    window = Tk()
    window.withdraw()
    radius = simpledialog.askfloat(title="Question", prompt="What is the radius of the circle?")
    aOrC = simpledialog.askstring(title="Question", prompt="Do you want to calculate the area or circumference?")
    if aOrC == "area":
        messagebox.showinfo(message = "Area: " + str(math.pi*radius*radius))
    elif aOrC == "circumference":
        messagebox.showinfo(message = "Circumference: " + str(2 * math.pi * radius))
#Area = πr^2
#Circumference = 2πr 