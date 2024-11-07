from tkinter import *

import sys

root = Tk()

class Application3():
    def __init__(self):

        self.root = root
        self.tela3()
        self.CriandoBotao()
        root.mainloop()

    def callTela2(self):

        
        sys.path.append('D:/Users/Alex Silva/Documents/Tkinter/TesteDeTela/PacoteTela2')
        import tela2

    def tela3(self):

        self.root.title("Teste de tela 3")
        self.root.configure(background='lightpink')
        self.root.geometry("1080x720")
        self.root.resizable(True, True)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=800, height=600)

    def CriandoBotao(self):
        self.btnTela2 = Button(text="Tela2", command=self.callTela2)
        self.btnTela2.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

Application3()