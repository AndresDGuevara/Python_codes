from tkinter import *

def LoginPage():
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")

    Label(login_screen, text = "Please enter login details").pack()
    Label(login_screen, text = "").pack()
    Label(login_screen, text = "Username").pack()

    username_login_entry = Entry(login_screen, textvariable = "Username")
    username_login_entry.pack()

    Label(login_screen, text = "").pack()
    Label(login_screen, text = "Password").pack()

    password_login_entry = Entry(login_screen, textvariable = "Password", show = '*')
    password_login_entry.pack()

    Label(login_screen, text = "").pack()
    Button(login_screen, text = "Login", width = 10, height = 1).pack()
    login_screen.mainloop()

LoginPage()