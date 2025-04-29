import tkinter as tk
from tkinter import ttk

import card_rd


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x500')
        self.title('Daily Tarot Reading')

        ttk.Label(self,
                text="Single Card Reading", font=('Times New Roman', 18)
                ).pack(side=tk.TOP, pady=20)

        ttk.Label(self,
                text="Just relax. Clear your mind.\nTake a couple of slow breaths. Think about what area of your life needs guidance; or of a problem that you would like to solve. Or think about a yes-no question.\n\nWhile you are ready, press the buttom to draw a card.",
                font=('Times New Roman', 11), wraplength=340, justify=tk.CENTER
                ).pack(side=tk.TOP)

        # place a button on the root window
        ttk.Button(self,
                text="Draw",
                command=self.open_window1).pack(side=tk.TOP, pady=20)
        

        ttk.Label(self,
                text="Pasr, Present, Future", font=('Times New Roman', 18)
                ).pack(side=tk.TOP, pady=20)

        ttk.Label(self,
                text="Simple spread involves reading your past, present, and future regarding a particular situation in your life.",
                font=('Times New Roman', 11), wraplength=340, justify=tk.CENTER
                ).pack(side=tk.TOP)

        # place a button on the root window
        ttk.Button(self,
                text="Draw",
                command=self.open_window2).pack(side=tk.TOP, pady=20)

    def open_window1(self):
        card_rd.sc__main__()

    def open_window2(self):
        card_rd.c3__main__()



if __name__ == "__main__":
    app = App()
    app.mainloop()