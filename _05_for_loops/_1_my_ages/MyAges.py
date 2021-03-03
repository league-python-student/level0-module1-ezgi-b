from tkinter import Tk, simpledialog

if __name__ == "__main__":
    window = Tk()
    window.withdraw()
    age = simpledialog.askinteger("Question", "What is your age?")
    print('These are the ages you have been alive for:')
    for i in range(age + 1):
        print(i)