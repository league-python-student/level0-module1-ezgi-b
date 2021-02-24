'''
* Write a python program that asks the user a minimum of 3 riddles.


* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
'''
from tkinter import simpledialog, messagebox, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    riddle1 = "What has two hands but isn't alive? (answer in the format 'a (noun)')"
    answer1 = "a clock"
    riddle2 = "What room has no walls and no ceiling? (answer in the format 'a (noun)')"
    answer2 = "a mushroom"
    riddle3 = "What word becomes shorter if you add two letters to it? (answer is just the word)"
    answer3 = "short"
    correctNum = 0

    for i in range(3):
        if i == 0:
            riddle = riddle1
            answer = answer1
        elif i == 1:
            riddle = riddle2
            answer = answer2
        elif i == 2:
            riddle = riddle3
            answer = answer3
        testAnswer = simpledialog.askstring(title="Riddle", prompt=riddle)

        if testAnswer.lower() == answer.lower():
            messagebox.showinfo(message="Correct!")
            correctNum += 1
        else:
            messagebox.showerror(message="That is incorrect! The correct response was " + answer + ".")

    messagebox.showinfo(title="End", message="You got " + str(correctNum) + "/3 points.")

