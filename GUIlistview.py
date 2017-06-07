import Tkinter as tk
import login
import GUIbutton

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'LOGIN', width = 25, command = self.new_window)
        self.button1.configure(bg='blue',fg='white',bd=10)
        self.button1.pack()
        self.frame.pack()

        self.quitButton = tk.Button(self.frame, text = 'CONVERTER', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.quitButton.configure(bg='orange',fg='black',bd=10)
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = login.login(self.newWindow)

    def close_windows(self):
        self.master.GUIbutton.GUIbutton()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    login.foo()
    GUIbutton.bar()

