from tkinter import *
from tkinter import messagebox

log = Tk()
log.geometry("500x500")
log.title("User login")
log.config(bg="#5900D3")

# name = input("Enter username: ")
# pword = input("Enter password: ")



# Creating labels
account = Label(log, text="Already have an account?", bg="#5900D3", font=("consoles 15 bold"))
use = Label(log, text="Please enter your username:", bg="#5900D3")
word = Label(log, text="Please enter your password:", bg="#5900D3")

# Creating entries
user = Entry(log)
passw = Entry(log, show="*")

def submit():
    usernames = ["Zaid", "Aaliyah", "Lithe", "Thabo", "Zoe"]
    passwords = ["1000", "5566", "7700", "1244", "4953"]
    found = False
    for x1 in range(len(usernames)):
        if user.get() == usernames[x1] and passw.get() == passwords[x1]:
            found = True
    if found == True:
        messagebox.showinfo("Access", "!!Granted!!")
        log.destroy()
        import sorting

    else:
        messagebox.showerror("Access", "!!Denied!!")

def clear_all():
    user.delete(0, END)
    passw.delete(0, END)

def exit_program():
    return log.destroy()

# Creating buttons
lin = Button(log, text="Login", borderwidth="10", command=submit)
clear = Button(log, text="Clear", borderwidth="10", command=clear_all)
exit = Button(log, text="Exit", borderwidth="10", command=exit_program)

# Placing labels
account.place(x=125, y=25)
use.place(x=20, y=100)
word.place(x=20, y=150)

# Placing entries
user.place(x=250, y=100)
passw.place(x=250, y=150)


# Placing buttons
lin.place(x=220, y=250)
clear.place(x=50, y=350)
exit.place(x=390, y=350)

log.mainloop()
