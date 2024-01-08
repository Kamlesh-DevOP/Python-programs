from random import *
from tkinter import *
import os

def Guess_Checker(Guess):    
                       #FUNCTION TO CHECK THE GUESS
    answer_list = list()
    guess_list = list()                   
    for i in range(len(Answer)):
        answer_list.append([Answer[i], 0])
        guess_list.append([Guess[i], 0])
    for i in range(len(Answer)):
        if guess_list[i][0] == answer_list[i][0]:
            letter_input[i+active_lettercount-5]["bg"] = "#518233"
            guess_list[i][1] = 1
            answer_list[i][1] = 1
    for i in range(len(Answer)):
        for j in range(len(Answer)):
            if (guess_list[i][1] == answer_list[j][1] == 0) and (guess_list[i][0] == answer_list[j][0]):
                letter_input[i+active_lettercount-5]["bg"] = "#a3a334"
                answer_list[j][1] = 1
    if Guess == Answer:                            
        result = True           #IF GUESS IS ANSWER, RUN winner()
        winner()

def winner():
    global winner_frame
    winner_frame = Frame(root)
    winner_frame.pack()
    won = Label(winner_frame, text = f"You Won with {active_lettercount//5} guess(es)! ",font = ("Times", 25))
    won.grid(column = 2)
    exitgame = Button(winner_frame, text = "Quit", command = lambda : root.destroy())                             #Function to make labels after win
    exitgame.grid(column = 2)
    replay = Button(winner_frame, text = "New Game", command = winner2)
    replay.grid(column = 2)
    
def winner2():
    winner_frame.destroy()                                               #Makeshift function to delete endgame frame
    window()

def loser():
    global loser_frame
    loser_frame = Frame(root)
    loser_frame.pack()
    lost = Label(loser_frame,text = f"You Lost! Better Luck Next time! The word was {Answer}", font = ("Times", 25))
    lost.grid(column = 2)                                                                                         #Function to make Labels after loss
    exitgame2 = Button(loser_frame, text = "Quit", command = lambda : root.destroy())
    exitgame2.grid(column = 2)
    replay2 = Button(loser_frame, text = "New Game", command = loser2)
    replay2.grid(column = 2)

def loser2():
    loser_frame.destroy()                                                #Makeshift function to delete loser frame 
    window()

def key_binder(event):
    global active_lettercount, Guess
    if (event.char >= "a" and event.char <= "z") or (event.char >= "A" and event.char <= "Z"): 
        letter_input[active_lettercount]["text"] = event.char.upper()                          #Button gets text everytime key is pressed
        active_lettercount += 1
        Guess = Guess + event.char.upper()                                 #Guess gets updated
        if active_lettercount % 5 == 0:
            if active_lettercount == 30:
                if Guess == Answer:
                    pass
                else:
                    loser()                                       

def enter(event):
    global Guess
    if active_lettercount%5 == 0:
        Guess_Checker(Guess)
        Guess = ""

def backspace(event):
    global active_lettercount, Guess
    if Guess != "":                         #Backspace functionality
        letter_input[active_lettercount-1]["text"] = ""
        active_lettercount -= 1
        Guess=Guess[:-1]


def window():    
    global frame, active_lettercount, result, Answer
    letter_input.clear()
    frame.destroy()
    frame = Frame(root,bg = "#000000")
    frame.pack()
    active_lettercount = 0
    result = False
    Answer = choice(words).upper()
    for i in range(3,9):
        for j in range(5):                                             #Two loops to display buttons in 5x6 form.
            Input_Button = Button(frame, text = "", width = 7, height = 4, bg = "#373b39", fg = "#ffffff", font = ("Times", 15))
            Input_Button.grid(row = i, column = j, padx = 3, pady = 3)
            letter_input.append(Input_Button)

def rungame():
    global Guess,letter_input,active_lettercount,result,titlee,words
    root = Tk()
    frame = Frame(root, bg = "#73706f")
    frame.pack(ipadx = 20)
    root.minsize(465,753)
    root.title("Wordle Remake")
    Guess = ""
    with open("wordle kamlesh\wordle_words.txt", "r") as f:
        words = f.read().splitlines()
    letter_input = []                                  #Store "address" of buttons, to change color.
    active_lettercount = 0                             #Keep track of lines
    result = False
    titlee = Label(root, text = "WORDLE", font = ("Times",40), bg = "#000000", fg = "#ffffff")        
    titlee.pack(ipadx = 10, ipady = 10, fill = X)
    root.bind("<BackSpace>", backspace)
    root.bind("<Key>", key_binder)                                             #Event bind
    root.bind("<Return>", enter)
    window()
    Menubar = Menu(root)
    New_Menu = Menu(Menubar, tearoff = 0)
    Menubar.add_cascade(label = "Options", menu = New_Menu)
    New_Menu.add_command(label = "New Game", command = window)
    New_Menu.add_command(label = "Exit", command = lambda: root.destroy())
    root.config(menu = Menubar)
    root.mainloop()
