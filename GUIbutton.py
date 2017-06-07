from tkinter import *
import tkinter as tk
import ttk

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        
        self.button1 = Button(frame, text="SELECT FILE")
        self.button1.pack(side=LEFT)
        self.button1.configure(bg='red', fg='white',bd=8)

        self.button1 = Button(frame, text="CONVERSION", command=self.conv)
        self.button1.pack(side=LEFT)
        self.button1.configure(bg='tan', fg='black',bd=8)

        self.button2 = Button(frame, text="CONVERT")
        self.button2.pack(side=LEFT)
        self.button2.configure(bg='navy', fg='white',bd=8, width=16)

        self.button1 = Button(frame, text="RESULT:DOWNLOAD")
        self.button1.pack(side=LEFT)
        self.button1.configure(bg='green', fg='white',bd=8)

       
    def conv(self):
       s = Tkinter.Scrollbar()
       L = Tkinter.Listbox()

       s.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
       L.pack(side=Tkinter.LEFT, fill=Tkinter.Y)

       s.config(command=L.yview)
       L.config(yscrollcommand=s.set)

       notes=['PDF TO DOC','PDF TO TEXT','PDF TO IMAGE','TEXT TO PDF','TEXT TO DOC','TEXT TO IMAGE','DOC TO PDF',
             'DOC TO TEXT','DOC TO IMAGE','IMAGE TO TEXT','IMAGE TO PDF','IMAGE TO DOC']

       for note in notes:
            L.insert(Tkinter.END, str(note))
            

root = Tk()
app = App(root)
root.mainloop()
