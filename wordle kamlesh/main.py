from customtkinter import *
import csv
from tkinter import *
import game

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

#login tab
userid_login_entry=CTkEntry(tab1, placeholder_text='Enter User ID', width=300)
userid_login_entry.grid(row=0, padx=50, pady=10, sticky="ew")
pwd_login_entry=CTkEntry(tab1, placeholder_text= 'Enter Password', show='*')
pwd_login_entry.grid(row=1, padx=50, pady=10, sticky="ew")
def loginshowpassword():
    if pwd_login_entry.cget('show')=='*':
        pwd_login_entry.configure(show='')
    else:
        pwd_login_entry.configure(show='*')
login_passwordstatus=StringVar(value='showing')
login_showpass=CTkCheckBox(tab1, text='Show password', variable=login_passwordstatus, command=loginshowpassword, font=('book antiqua', 15))
login_showpass.grid(row=2, padx=50, pady=10, sticky="ew")
def on_login_submit():
    userid=userid_login_entry.get()
    pwd=pwd_login_entry.get()
    with open(r'wordle kamlesh\userdetails.csv','r') as f:
        r=csv.reader(f)
        for i in r:
            if i==[userid,pwd]:
                loginsuccess=1
                break
        if loginsuccess:
                signupwindow.destroy()
                game.rungame()
        else:
            if pwd=='' or userid=='':
                messagebox.showerror("Error","Empty field(s). Please fill all the fields")
            else:
                messagebox.showerror('Wrong credentials','Please check your credentials.')
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
    userid=signup_userid_entry.get()
    pwd=signup_pwd_entry.get()
    confirm=signup_confirmpass_entry.get()
    if confirm==pwd:
        with open(r'wordle kamlesh\userdetails.csv', 'a', newline='') as f:
            w=csv.writer(f)
            w.writerow([userid, pwd])
        signupwindow.destroy()
        game.rungame()
    else:
        if pwd=='' or confirm=='' or userid=='':
            messagebox.showerror("Error","Empty field(s). Please fill all the fields")
        else: 
            messagebox.showerror("Error","Password and Confirm password fields don't match") 
signup_submit_button=CTkButton(tab2, text='Submit', command= on_signup_submit)
signup_submit_button.grid(row=4, padx=50, pady=10, sticky="ew")

signupwindow.mainloop()