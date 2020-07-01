from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

window = Tk()
window.title("Hangman")

words = ["SCIENCE","ENGINEERING","COMPUTER","DICTIONARY","BOOK","LAPTOP","ARTIFICIAL","INTELLIGENCE","MACHINE",
        "LEARNING","AUTOPILOT","FIGHTER","CRUISE","UNIVERSITY","COUNTRY","VEHICLE","HELICOPTER","BOEING"]

photos = [PhotoImage(file="images/hang0.png"),PhotoImage(file="images/hang1.png"),PhotoImage(file="images/hang2.png"),
        PhotoImage(file="images/hang3.png"),PhotoImage(file="images/hang4.png"),PhotoImage(file="images/hang5.png"),
        PhotoImage(file="images/hang6.png"),PhotoImage(file="images/hang7.png"),PhotoImage(file="images/hang8.png"),
        PhotoImage(file="images/hang9.png"),PhotoImage(file="images/hang10.png"),PhotoImage(file="images/hang11.png"),]

def newGame():
    global word_withspaces
    global numberOfGuesses
    numberOfGuesses = 0
    imgLabel.config(image=photos[0])
    word = random.choice(words)
    word_withspaces = " ".join(word)
    labelWord.set(" ".join("_"*len(word)))

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < 11:
        txt = list(word_withspaces)
        guessed = list(labelWord.get())
        if word_withspaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                labelWord.set("".join(guessed))
                if labelWord.get() == word_withspaces:
                    messagebox.showinfo("Hangman","You guessed it correct!!!")
        else:
            numberOfGuesses += 1
            imgLabel.config(image = photos[numberOfGuesses])
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman","Game Over")


imgLabel = Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
imgLabel.config(image=photos[0])
labelWord = StringVar()
Label(window, textvariable=labelWord, font=("Consolas 24 bold")).grid(row=0,column=3,columnspan=6,padx=10)


n = 0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=("Helvetica 16"), width=4).grid(row=1+n//9, column=n%9)
    n+=1

Button(window, text="New\nGame", command = lambda:newGame(),font=("Helvetica 14")).grid(row=3,column=8,sticky="NSWE")

newGame()
window.mainloop()