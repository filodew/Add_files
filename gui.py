import time
from script import *
import os
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def Login_enter():
    global com_name_e
    global pass_e
    global roots
    #global c_name

    roots = Tk()
    roots.title('uh file adder')
    # root.iconbitmap('C:\uhfa\Tkinter')
    roots.geometry("400x200")

    # creating a Label widget
    myLabel0 = Label(roots, width=14)
    myLabel1 = Label(roots, text="Update helper files Adder")
    myLabel2 = Label(roots, text="Company Name")
    myLabel3 = Label(roots, text="Password")

    # input fields - enter login and password
    com_name_e = Entry(roots, width=30)

    pass_e = Entry(roots, width=30, show='*')
    #pass_e.insert(0, "Enter your password")
    # Login button
    Login_button = Button(roots, text="Log in", command=FSLogin) # This creates the button with the text 'signup', when you click it, the command 'FSLogin' will run. which is the def

    # elements location
    myLabel0.grid(row=0, column=0)
    myLabel1.grid(row=0, column=1)
    myLabel0.grid(row=1, column=1)
    myLabel0.grid(row=2, column=1)
    myLabel2.grid(row=3, column=1)
    com_name_e.grid(row=4, column=1)
    myLabel3.grid(row=6, column=1)
    pass_e.grid(row=8, column=1)
    myLabel0.grid(row=9, column=0)
    Login_button.grid(row=10, column=1)

    roots.mainloop() # This just makes the window keep open


def FSLogin():
    #global c_name
    with open(creds, 'w') as f:  # Creates a document using the variable at the top.
        f.write(com_name_e.get())  # com_name_e is the variable which storing the input to. Tkinter makes use .get() to get the actual string.
        f.write('\n')  # splits the line so both variables are on different lines.
        f.write(pass_e.get())  # Same as com_name_e.get just with pword var
        f.close()  # closes the file

    roots.destroy()  # This will destroy the signup window.
    Logged()  # This will move us onto the add_uhfile definition.


def Logged():
    global rootA

    rootA = Tk()  # This now makes a new window.
    rootA.geometry("400x200")
    rootA.title('Logged')  # This makes the window title 'login'

    # Text labels
    myLabel11 = Label(rootA, text="Update helper files Adder")
    myLabel11.grid(row=1, column=1)
    myLabel12 = Label(rootA, text="You're logged in.")
    myLabel12.grid(row=2, column=1)
    myLabel13 = Label(rootA, text=" ")
    myLabel13.grid(row=3, column=0)


    # Continuation of text labels
    myLabel15 = Label(rootA, text="Please add files to the folder: uhfa/things!")
    myLabel15.grid(row=7, column=1)
    myLabel16 = Label(rootA, text=" ")
    myLabel16.grid(row=8, column=0)

    # Start script button
    Start_script = Button(rootA, text="Start script", command=Add_uhfile)
    Start_script.grid(row=10, column=1)

    # The script does its job
    rootA.mainloop()


if os.path.isfile(creds):
    Login_enter()
else:
    Logged()
