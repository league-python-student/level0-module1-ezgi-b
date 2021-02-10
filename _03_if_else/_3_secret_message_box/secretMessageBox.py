from tkinter import simpledialog, messagebox, Tk
if __name__ == "__main__":
    password = "tohatlakataowrta"
    window = Tk()
    window.withdraw()
    secretMsg = simpledialog.askstring(title="Question", prompt="Type in a secret message.")
    guess = simpledialog.askstring(title="Lock", prompt="To open the Secret Message Box, type in the correct password.")
    if guess == password:
        messagebox.showinfo(title="Yay!", message="The secret message is this: " + secretMsg)
    else:
        messagebox.showerror(title="ERROR", message="INTRUDER, INTRUDER!!!!!!!!")
