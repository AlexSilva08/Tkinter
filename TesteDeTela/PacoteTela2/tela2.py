from tkinter import *

import sys


root = Tk()

class Application2():
    def __init__(self):

        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):

        self.root.title("Teste de tela 2")
        self.root.configure(background='lightgreen')
        self.root.geometry("1080x720")
        self.root.resizable(True, True)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=800, height=600)

Application2()