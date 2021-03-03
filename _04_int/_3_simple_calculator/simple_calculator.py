# Write a Python program that asks the user for two numbers.
# Then ask the user if the would like to add, subtract, multiply, or divide.
# Use if-else statements to provide the desired math operation on the numbers and display the result.
from tkinter import simpledialog, Tk, messagebox
if __name__ == "__main__":
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askfloat(title="Question", prompt="Enter the first number")
    num2 = simpledialog.askfloat(title="Question", prompt="Enter the second number")
    operation = simpledialog.askstring(title="Question", prompt="Would you like to add, subtract, multiply, or divide (a, s, m, d)")
    finalNum = 0
    if operation == 'a':
        finalNum = num1 + num2
    elif operation == 's':
        finalNum = num1 - num2
    elif operation == 'm':
        finalNum = num1*num2
    elif operation == 'd':
        finalNum = num1/num2

    messagebox.showinfo(None, "The result is " + str(finalNum))