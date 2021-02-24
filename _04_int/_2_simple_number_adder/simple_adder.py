# Write a Python program that asks the user for two numbers. 
# Then display the sum of the two numbers
from tkinter import Tk, simpledialog, messagebox
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askfloat(title="First Number", prompt="Enter a number")
    num2 = simpledialog.askfloat(title="Second Number", prompt="Enter a second number")
    sum = num1 + num2

    messagebox.showinfo(message="The sum of the two numbers you entered is " + str(sum) + ".")