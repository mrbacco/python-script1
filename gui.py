#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

class App(tk.Frame):

    def __init__(self, master=None):
        super(App, self).__init__(master)
        self.grid()  
        self.createWidgets()
 #       self.delButton()

    def createWidgets(self):
        self.mondialLabel = tk.Label(self, text=' BAC GUI applet with Python')
        self.mondialLabel.config(bg="#00ffff")
        self.mondialLabel.grid()
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()
        self.newButton = tk.Button(self, text='New Widget', command=self.createWidgets)
        self.newButton.grid()
#        self.delButton = tk.Button(self, text = "Delete Widget", command=self.delButton)        
#        self.delButton.grid()
        
        
app = App()
app.master.title('BAC')
app.mainloop()
