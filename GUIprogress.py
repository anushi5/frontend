import Tkinter as tk
import ttk


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button = ttk.Button(text="CONVERT", command=self.start)
        self.button.pack()
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack()

        self.bytes = 0
        self.maxbytes = 0

    def start(self):
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000
        self.read_bytes()

    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 500
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)

app = SampleApp()
app.mainloop()
"""
from Tkinter import *
import ttk
import time

MAX = 30

root = Tk()
root.geometry('{}x{}'.format(400, 100))
progress_var = DoubleVar() #here you have ints but when calc. %'s usually floats
theLabel = Label(root, text="Sample text to show")
theLabel.pack()
progressbar = ttk.Progressbar(root, variable=progress_var, maximum=MAX)
progressbar.pack(fill=X, expand=1)


def loop_function():

    k = 0
    while k <= MAX:
    ### some work to be done
        progress_var.set(k)
        k += 1
        time.sleep(0.02)
        root.update_idletasks()
    root.after(100, loop_function)

loop_function()
root.mainloop()
"""
