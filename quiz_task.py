''' Week 9 Quiz Task '''

from tkinter import *

CITIES = [
    "Auckland",
    "Queenstown",
    "Northland",
    "Bay of Plenty",
    "Taranaki",
    "Wellington",
    "Manukau",
    "Manurewa",
    "East Tamaki"
]

CAPITAL_CITY = "Wellington"

class Quiz:
    def __init__(self, root):
        self.root = root

        def radio(frame, text, var):
            btn = Radiobutton(frame, text = text, variable = var, value = text, command = self.update)
            btn.grid(sticky=W)
    
        self.city_var = StringVar()
        self.city_var.set("?")

        cities_frame = Frame(root)
        answer_frame = Frame(root)
        cities_frame.grid()
        answer_frame.grid()

        l1 = Label(cities_frame, text = "What Is The Capital Of New Zealand?")
        l1.grid()

        self.l2 = Label(answer_frame, text = "")
        self.l2.grid()

        for city in CITIES:
            radio(cities_frame, city, self.city_var)

    def update(self):
        if self.city_var.get() == "Wellington":
            self.l2.configure(text = "Correct")
        else:
            self.l2.configure(text = "Incorrect")


if __name__ == '__main__':
    root = Tk()
    root.title("Fun With Cats")
    Quiz(root)
    root.update()
    root.mainloop()