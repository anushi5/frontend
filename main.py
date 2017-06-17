import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
from tkinter.filedialog import askopenfilename
from engine import *
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
        container.configure(background='grey')
        self.frames = {}
        for F in (LoginPage, HomePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=1, column=1, sticky="nsew")
            container.grid_rowconfigure(0, weight=1)
            container.grid_rowconfigure(2, weight=1)
            container.grid_columnconfigure(0, weight=1)
            container.grid_columnconfigure(2, weight=1)

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.configure(background='grey')
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
        label = tk.Label(self, text="Welcome to Multi Document-converter", fg="Black",bg="grey",font=("Calibri", 25,"bold"))
        label.grid(columnspan=2)

        name = tk.Label(self, text='Username : ',fg="black",bg='grey',font=("Calibri", 17)) # More labels
        password = tk.Label(self, text='Password : ',fg="black",bg='grey',font=("Calibri", 17)) # ^
        name.grid(row=1,columnspan=1,pady=20)
        password.grid(row=2,columnspan=1,pady=20)
     
        namevalue = tk.Entry(self) # The entry input
        passwordvalue = tk.Entry(self, show='*')
        namevalue.grid(row=1, column=1,pady=20,columnspan=2,sticky='EWNS')
        passwordvalue.grid(row=2, column=1,pady=20,columnspan=2,sticky='EWNS')

        button = tk.Button(self, text="Login",command=lambda: checkAuth(namevalue.get(),passwordvalue.get(),controller),bd='2',activebackground='red',activeforeground='white',width=5,fg="black",bg="white",font=("Calibri", 15))
        button.grid(row=3,column=1,pady=10,sticky=E)
        


class HomePage(tk.Frame):
    
    def __init__(self, parent, controller):
      self.filename = ""
      tk.Frame.__init__(self, parent)
      self.controller = controller
      label = tk.Label(self, text="Document-converter", fg="black",bg="grey", font=("Calibri", 25,"bold"))
      label.grid(columnspan=1)
      
      # Dropdown Menu
      optionList = ["PDF to Text","PDF to Doc","Text to Doc","Doc to Text","Image to Text","Text to Image","Image to Doc","Doc to Image","Image to PDF"]
      dropVar=StringVar()
      dropVar.set("Conversion Type") # default choice
      dropMenu1 = OptionMenu(self, dropVar, *optionList)
      dropMenu1.config(bg='green',fg='white',bd='8',font=("Calibri",17))
      dropMenu1["menu"].config(bg="WHITE",fg="green",activebackground='grey',bd='6',font=("Calibri",17))
      dropMenu1.grid(row=1, column=1,columnspan=1)

      browse = tk.Button(self, text='Browse', command=self.browsefile,fg="white",bd='8',bg="green",font=("Calibri", 17))
      browse.grid(row=1,column=2,padx=20,pady=20,sticky='EWNS')
      
      name = tk.Label(self, text='Enter Filename To Be Saved : ',fg="white",bg="grey",font=("Calibri", 17)) # More labels
      name.grid(row=2,padx=20, pady=20)
      namevalue = tk.Entry(self,width=30) # The entry input
      namevalue.grid(row=2, column=1,padx=0, pady=20,columnspan=2,sticky='EWNS')
      

      submitbtn = tk.Button(self, text="Submit",fg="white",bd='8',bg="green",font=("Calibri", 17),command=lambda: convertfile(self.filename,dropVar.get(),namevalue.get()))
      submitbtn.grid(row=3, column=1,columnspan=3,padx=20,pady=20,sticky='EWNS')

    def browsefile(self):
      self.filename = askopenfilename()
      print(self.filename)
    


if __name__ == "__main__":
    app = SampleApp()
app.mainloop()
