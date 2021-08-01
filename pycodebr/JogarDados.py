import random
from tkinter import *

class RolarDados(object):

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(master, font = ("times", 200))
        bottom = Button(master, text = "Role os Dados", command = self.rolar)
        bottom.place(x = 200, y = 0)

    def rolar(self):
        simbolos = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        self.label.config(text = f"{random.choice(simbolos)}{random.choice(simbolos)}")
        self.label.pack()

if __name__ == "__main__":
    invoke = Tk()
    invoke.title("Jogue os Dados e veja o Resultado")
    invoke.geometry("500x300")
    RolarDados(invoke)
    invoke.mainloop()