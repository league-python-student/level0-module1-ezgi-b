from tkinter import messagebox, simpledialog, Tk
if __name__ == "__main__":
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(title="Question", prompt="What is your first name?")
    if name=="Demir":
        messagebox.showinfo(title="FACTS!", message="You take a Python class, and your name is 5 letters long!")
    elif name=="Ronald":
        messagebox.showinfo(title="FACTS!", message="You take a Python class, and your name is 6 letters long!")
    elif name=="Isaac":
        messagebox.showinfo(title="FACTS!", message="You take a Python class, and your name is 5 letters long!")
    elif name=="Ezgi":
        messagebox.showinfo(title="FACTS!", message="You take a Python class, and your name is 4 letters long!")
    elif name=="Daniel":
        messagebox.showinfo(title="FACTS!", message="You teach a Python class, and your name is 6 letters long!")
    else:
        messagebox.showerror(title="ERROR", message="You aren't in this class!")






