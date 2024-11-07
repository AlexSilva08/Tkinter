from tkinter import *

import sys

root = Tk()

class Application2():
    def __init__(self):

        self.root = root
        self.tela2()
        self.CriandoBotao()
        root.mainloop()

    def callTela1(self):

        
        sys.path.append('D:/Users/Alex Silva/Documents/Tkinter/TesteDeTela/PacoteTela1')
        import tela1

    def tela2(self):

        self.root.title("Teste de tela 2")
        self.root.configure(background='lightgreen')
        self.root.geometry("1080x720")
        self.root.resizable(True, True)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=800, height=600)

    def CriandoBotao(self):
        self.btnTela1 = Button(text="Tela1", command=self.callTela1)
        self.btnTela1.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

Application2()