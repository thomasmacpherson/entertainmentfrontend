#!/usr/bin/python
from Tkinter import *
from ttk import Frame, Label, Style
from ttk import Entry
from PIL import Image, ImageTk
import os
import subprocess
import tkFont
os.chdir("/home/pi/python_games/")
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
         
        self.initUI()      
        
    def initUI(self):

        # Style().configure("TButton", padding=(10, 10, 10, 10), 
        #     font='serif 8', weight=1)
        mri = Image.open("mri.jpg")
        # mri.resize((w, h), Image.ANTIALIAS)
        background_image=ImageTk.PhotoImage(mri)
        background_label = Label(self, image=background_image)
        background_label.photo=background_image
        background_label.place(x=0, y=0, relheight=1)        
        self.columnconfigure(0, pad=10, weight=1)
        self.columnconfigure(1, pad=10, weight=1)
        self.columnconfigure(2, pad=20, weight=1)
        self.rowconfigure(0, pad=20, weight=1)
        self.rowconfigure(1, pad=20, weight=1)
        self.rowconfigure(2, pad=20, weight=1)
        self.customFont = tkFont.Font(family="Helvetica", size=15)
        # Style().configure('green/black.TButton', foreground='yellow', background=tk_rgb, activefill="red",font=self.customFont)
        entry = Entry(self) #TODO: REMOVE?
        f = open('games.txt')
        buttonArray = []
        for i, line in enumerate(f):
        	line = line.split(':')
        	filename = line[0].translate(None, ' \n').lower()
        	imagefile = Image.open(filename + "-thumbnail.png")
        	image = ImageTk.PhotoImage(imagefile)
        	label1 = Label(self, image=image)
        	label1.image = image                         # + "\n" + line[1]
        	tk_rgb = "#%02x%02x%02x" % (100+35*(i%5), 50+100*(i%3), 70+80*(i%2))
        	button = (Button(self, text=line[0], image=image, compound="bottom", bd=0, bg=tk_rgb, font=self.customFont, command = lambda filename=filename :os.system("python " + filename + ".py")))
        	button.grid(row=i/3, column=i%3)
        f.close()
        
        self.pack(fill=BOTH, expand=1)

def main():
  
    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))


    # root.lower()
    # pad = 20
    # root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad)) 
    root.overrideredirect(True)
    app = Example(root)
    app.pack(fill=BOTH, expand=1)
    root.mainloop()  


if __name__ == '__main__':
    main()  
