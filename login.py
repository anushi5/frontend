from tkinter import *
import os
 
creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'
 
def Signup(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
 
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Signup') # This renames the title of said window to 'signup'
    intruction = Label(roots, text='Please Enter new Credidentials\n') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0, sticky=E) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    nameL = Label(roots, text='New Username: ') # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ') # ^^
    nameL.grid(row=1, column=0, sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=0, sticky=W) # ^^
 
    nameE = Entry(roots) # This now puts a text box waiting for input.
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE.grid(row=2, column=1) # ^^
 
    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop() # This just makes the window keep open, we will destroy it soon
 
def FSSignup():
    with open(creds, 'w') as f: # Creates a document using the variable we made at the top.
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.close() # Closes the file
 
    roots.destroy() # This will destroy the signup window. :)
    Login() # This will move us onto the login definition :D
 
def Login():
    global nameEL
    global pwordEL # More globals :D
    global root
 
    root = Tk() # This now makes a new window.
    
    w = 500
    h = 300
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (500, 300, x, y))
    root.title('User Login') # This makes the window title 'login'
    loginframe = Frame(root,height=w,width=h)
    loginframe.pack()
    loginframe.grid(padx=20, pady=20)
    intruction = Label(loginframe, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
 
    name = Label(loginframe, text='Username : ') # More labels
    password = Label(loginframe, text='Password : ') # ^
    name.grid(row=1, column=1,columnspan=1, padx=20, pady=20)
    password.grid(row=2, column=1,columnspan=1, padx=20, pady=20)
 
    namevalue = Entry(loginframe) # The entry input
    passwordvalue = Entry(loginframe, show='*')
    namevalue.grid(row=1, column=2, columnspan=3, padx=10, pady=20)
    passwordvalue.grid(row=2, column=2, columnspan=3, padx=10, pady=20)
 
    loginB = Button(loginframe, text='Login', command=lambda:CheckLogin(namevalue.get(),passwordvalue.get())) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(column=4)
 
    loginframe.mainloop()
 
def CheckLogin():

    #directly bypass to main window
    '''with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        r = Tk() # Opens new window
        r.title(':D')
        r.geometry('150x50') # Makes the window a certain size
        rlbl = Label(r, text='\n[+] Logged In') # "logged in" label
        rlbl.pack() # Pack is like .grid(), just different
        r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()'''
 
def DelUser():
    os.remove(creds) # Removes the file
    rootA.destroy() # Destroys the login window
    Signup() # And goes back to the start!
 
Login()
'''if os.path.isfile(creds):
    Login()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()'''
