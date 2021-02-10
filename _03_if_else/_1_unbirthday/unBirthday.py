from tkinter import messagebox, simpledialog, Tk
from datetime import date

if __name__ == "__main__":
    t = date.today()
    print(t.strftime("%m/%d"))
    window = Tk()
    window.withdraw()
    birthday = simpledialog.askstring(title="Question", prompt="What is your birthday? (in mm/dd format)")
    if birthday==t.strftime("%m/%d"):
        messagebox.showinfo(title="info", message="Happy Birthday!")
    else:
        messagebox.showinfo(title="info", message="Have a very merry Unbirthday!")

