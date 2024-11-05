from tkinter import *

import sys

sys.path.append('C:/Users/user/Documents/kerygma/TesteDeTela/PacoteTela2')

root = Tk()


class Application():
    def __init__(self):

        self.root = root
        self.tela()
        self.CriandoBotao()
        root.mainloop()

    def ChamandoTela2(self):

        self.tela2()

    def tela(self):

        self.root.title("Teste de tela 1")
        self.root.configure(background='skyblue')
        self.root.geometry("1080x720")
        self.root.resizable(True, True)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=800, height=600)

    def CriandoBotao(self):
        self.btnTela2 = Button(text="Tela2" command=ChamandoTela2)
        self.btnTela2.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

Application()