from tkinter import *

import sys

telaAzul = Tk()

class Application1():
    def __init__(self):

        self.telaAzul = telaAzul
        self.tela1()
        self.CriandoBotao()
        telaAzul.mainloop()

    def callTela2(self):

        
        sys.path.append('D:/Users/Alex Silva/Documents/Tkinter/TesteDeTela/PacoteTela2')
        import tela2
        Application1() == tela2


    def tela1(self):

        self.telaAzul.title("Teste de tela 1")
        self.telaAzul.configure(background='skyblue')
        self.telaAzul.geometry("1080x720")
        self.telaAzul.resizable(True, True)
        self.telaAzul.maxsize(width=1920, height=1080)
        self.telaAzul.minsize(width=800, height=600)

    def CriandoBotao(self):
        self.btnTela2 = Button(text="Tela2", command=self.callTela2)
        self.btnTela2.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

Application1()