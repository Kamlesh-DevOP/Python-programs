from customtkinter import *
import csv
import tkinter as tk
from random import *

signupwindow=CTk()
signupwindow.iconbitmap('wordle project\icon.ico')
signupwindow.geometry('600x600')
signupwindow.minsize(600,600)
signupwindow.title('Wordle')
welcome=CTkLabel(signupwindow, text='Welcome to Wordle game', font=('book antiqua', 20))
welcome.pack(pady=50)
tab=CTkTabview(signupwindow)
tab.pack(pady=50)
tab1=tab.add('Login')
tab2=tab.add('Sign Up')

cur_streak=0
def get_cur_streak():
    global cur_streak
    with open(r'wordle project\scores.csv') as f:
        f.seek(0)
        r=csv.reader(f)
        for i in r:
            if i[0]==userid:
                cur_streak= int(i[1])

def inc_streak():
    global cur_streak
    with open(r'wordle project\scores.csv') as f:
        f.seek(0)
        r=csv.reader(f)
        l=[]
        for i in r:
            if i[0]==userid:
                l.append([i[0],int(i[1])+1])
                cur_streak= int(i[1])+1
            else:
                l.append(i)
    with open(r'wordle project\scores.csv','w', newline='') as f:
        f.seek(0)
        w=csv.writer(f)
        w.writerows(l)

def deletestreak():
    global cur_streak
    with open(r'wordle project\scores.csv') as f:
        f.seek(0)
        r=csv.reader(f)
        l=[]
        for i in r:
            if i[0]==userid:
                l.append([i[0],0])
                cur_streak= 0
            else:
                l.append(i)
    with open(r'wordle project\scores.csv','w', newline='') as f:
        f.seek(0)
        w=csv.writer(f)
        w.writerows(l)

def Guess_Checker(Guess):    #FUNCTION TO CHECK THE GUESS
    answer_list = []
    guess_list = []        
    print(Answer)   
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
        inc_streak()
        winner()

def winner():
    global winner_frame
    winner_frame = tk.Frame(root)
    winner_frame.pack()
    winner_frame.configure(bg = "#242c2c")
    won = tk.Label(winner_frame, text = f"You Won with {active_lettercount//5} guess(es)! ",font = ("Times", 25), bg='#242c2c', fg='#ffffff')
    won.grid(column = 2)
    exitgame = tk.Button(winner_frame, text = "Quit", font=('Times New Roman',25,'bold'),command = lambda: root.destroy())
    exitgame.grid(column = 2)
    replay = tk.Button(winner_frame, text = "New Game",font=('Times New Roman',25,'bold'), command = winner2)
    replay.grid(column = 2)

def winner2():
    winner_frame.destroy()
    root.destroy()
    rungame()

def loser():
    global loser_frame
    loser_frame = tk.Frame(root)
    loser_frame.pack()
    loser_frame.configure(bg = "#242c2c")
    lost = tk.Label(loser_frame, text = f"You Lost! Better Luck Next time! The word was {Answer}", font = ("Times", 25), bg = "#242c2c", fg='#ffffff')
    lost.grid(column = 2)                                                                                         #Function to make Labels after loss
    exitgame2 = tk.Button(loser_frame, text = "Quit",  font=('Times New Roman',25,'bold'),command = lambda : root.destroy())
    exitgame2.grid(column = 2)
    replay2 = tk.Button(loser_frame, text = "New Game",  font=('Times New Roman',25,'bold'),command = loser2)
    replay2.grid(column = 2)

def loser2():
    loser_frame.destroy()
    deletestreak()
    root.destroy()
    rungame()

def key_binder(event):
    global active_lettercount, Guess
    if (event.char >= "a" and event.char <= "z") or (event.char >= "A" and event.char <= "Z"): 
        letter_input[active_lettercount]["text"] = event.char.upper()  #Button gets text everytime key is pressed
        active_lettercount += 1
        Guess = Guess + event.char.upper()                             #Guess gets updated
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
    frame = tk.Frame(root,bg = "#000000")
    frame.pack()
    active_lettercount = 0
    result = False
    Answer = choice(words).upper()
    for i in range(3,9):
        for j in range(5):                                             #Two loops to display buttons in 5x6 form.
            Input_Button = tk.Button(frame, text = "", width = 7, height = 4, bg = "#373b39", fg = "#ffffff", font = ("Times", 15))
            Input_Button.grid(row = i, column = j, padx = 3, pady = 3)
            letter_input.append(Input_Button)

def rungame():
    global root,frame,Guess, Answer, letter_input, active_lettercount, result
    global titlee, Menubar, New_Menu, choice, words, cur_user, cur_streak, streaklabel
    root = tk.Tk()
    frame = tk.Frame(root, bg = "#73706f")
    frame.pack(ipadx = 20)
    root.title("Wordle")
    root.state('zoomed')
    root.minsize(465,1000)
    root.configure(bg='#242c2c')
    Guess = ""
    with open("D:\Kamlesh\Python\wordle project\wordle_words.txt", "r") as f:            #File with all possible 5 letter english words
        words = f.read().splitlines()
    letter_input = []                                  #Store "address" of buttons, to change color.
    active_lettercount = 0                             #Keep track of lines
    result = False
    titlee = tk.Label(root, text = "WORDLE", font = ("Times",40), bg = "#242c2c", fg = "#ffffff")     
    titlee.pack(ipadx = 10, ipady = 10, fill = X)
    streaklabel= tk.Label(root,text='{}\nCurrent Streak:{}'.format(cur_user, cur_streak), font = ("Times",20), bg = "#242c2c", fg = "#ffffff",justify='right', anchor=NE)
    streaklabel.pack(ipadx = 10, ipady = 1, fill= X) 
    root.bind("<BackSpace>", backspace)
    root.bind("<Key>", key_binder)
    root.bind("<Return>", enter)
    window()


#login tab
userid_login_entry=CTkEntry(tab1, placeholder_text='Enter User ID', width=300)
userid_login_entry.grid(row=0, padx=50, pady=10, sticky="ew")
pwd_login_entry=CTkEntry(tab1, placeholder_text= 'Enter Password', show='*')
pwd_login_entry.grid(row=1, padx=50, pady=10, sticky="ew")
cur_user=''
def loginshowpassword():
    if pwd_login_entry.cget('show')=='*':
        pwd_login_entry.configure(show='')
    else:
        pwd_login_entry.configure(show='*')
login_passwordstatus=StringVar(value='showing')
login_showpass=CTkCheckBox(tab1, text='Show password', variable=login_passwordstatus, command=loginshowpassword, font=('book antiqua', 15))
login_showpass.grid(row=2, padx=50, pady=10, sticky="ew")

userid=''
pwd=''
def on_login_submit():
    global cur_user, userid, pwd
    userid=userid_login_entry.get()
    pwd=pwd_login_entry.get()
    with open(r'wordle project\userdetails.csv', ) as f:
        r=csv.reader(f)
        data=list(r).copy() #using .copy and copying csv contents in another list because 'in' operator malfunctioned due to some reason
        if [userid,pwd] in data:
            cur_user=userid
            signupwindow.destroy()
            get_cur_streak()
            rungame()
        else:
            if pwd=='' or userid=='':
                tk.messagebox.showerror("Error","Empty field(s). Please fill all the fields")
            else:
                tk.messagebox.showerror('Wrong credentials','Please check your credentials.')
login_submit_button=CTkButton(tab1, text='Submit', command= on_login_submit)
login_submit_button.grid(row=3, padx=50, pady=10, sticky="ew")

#signup tab
def signupshowpassword():
    if signup_pwd_entry.cget('show')=='*':
        signup_pwd_entry.configure(show='')
        signup_confirmpass_entry.configure(show='')
    else:
        signup_pwd_entry.configure(show='*')
        signup_confirmpass_entry.configure(show='*')
signup_userid_entry=CTkEntry(tab2, placeholder_text='Create User ID', width=300)
signup_userid_entry.grid(row=0, padx=50, pady=10, sticky="ew")
signup_pwd_entry=CTkEntry(tab2, placeholder_text= 'Create Password', show='*')
signup_pwd_entry.grid(row=1, padx=50, pady=10, sticky="ew")
signup_confirmpass_entry=CTkEntry(tab2, placeholder_text= 'Confirm Password', show='*')
signup_confirmpass_entry.grid(row=2, padx=50, pady=10, sticky="ew")
signup_passwordstatus=StringVar(value='showing')
signup_showpass=CTkCheckBox(tab2, text='Show password', variable=signup_passwordstatus, command=signupshowpassword, font=('book antiqua', 15))
signup_showpass.grid(row=3, padx=50, pady=10, sticky="ew")

def on_signup_submit():
    global cur_user, pwd, userid
    userid=signup_userid_entry.get().strip()
    pwd=signup_pwd_entry.get().strip()
    confirm=signup_confirmpass_entry.get()
    is_userid_exists=False
    with open(r'wordle project\userdetails.csv',  ) as f:
        r=csv.reader(f)
        for i in r:
            if userid.lower()==i[0].lower():
                is_userid_exists=True
                tk.messagebox.showerror("Error","User id already exists. Please use a unique user id")

    if confirm==pwd and len(pwd)!=0 and not is_userid_exists:
        cur_user=userid
        with open(r'wordle project\userdetails.csv', 'a', newline='') as f, open(r'wordle project\scores.csv','a', newline='') as f1:
            w=csv.writer(f)
            w1=csv.writer(f1)
            w.writerow([userid, pwd])
            w1.writerow([userid,0])
        signupwindow.destroy()
        rungame()
    else:
        if pwd=='' or confirm=='' or userid=='':
            tk.messagebox.showerror("Error","Empty field(s). Please fill all the fields")
        else: 
            tk.messagebox.showerror("Error","Password and Confirm password fields don't match") 
signup_submit_button=CTkButton(tab2, text='Submit', command= on_signup_submit)
signup_submit_button.grid(row=4, padx=50, pady=10, sticky="ew")

signupwindow.mainloop()
