from tkinter import *

root = Tk()

class Application3():
    def __init__(self):

        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):

        self.root.title("Teste de tela 3")
        self.root.configure(background='lightpink')
        self.root.geometry("1080x720")
        self.root.resizable(True, True)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=800, height=600)

Application3()