import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, HomePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

def checkAuth(user,password,controller):
  #check Authetication using given parameters
  flag = True
  if flag:
    controller.show_frame("HomePage")

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Document-converter", font=controller.title_font)
        label.grid(columnspan=2)

        name = tk.Label(self, text='Username : ') # More labels
        password = tk.Label(self, text='Password : ') # ^
        name.grid(row=1,padx=20, pady=20)
        password.grid(row=2,padx=20, pady=20)
     
        namevalue = tk.Entry(self) # The entry input
        passwordvalue = tk.Entry(self, show='*')
        namevalue.grid(row=1, column=1,padx=20, pady=20,columnspan=2,sticky=W)
        passwordvalue.grid(row=2, column=1,padx=20, pady=20,columnspan=2,sticky=W)

        button = tk.Button(self, text="Login",command=lambda: checkAuth(namevalue.get(),passwordvalue.get(),controller))
        button.grid(row=3,column=1,padx=20, pady=20,sticky=E)
        


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Document-converter", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to Login page",
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()