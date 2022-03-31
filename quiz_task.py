''' Week 9 Quiz Task '''

from tkinter import *

CITIES = [
    "Auckland",
    "Wellington",
    "Northland",
    "Bay of Plenty",
    "Taranaki"
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
        cities_frame.grid()

        for city in CITIES:
            radio(cities_frame, city, self.city_var)

    def update(self):
        pass


if __name__ == '__main__':
    root = Tk()
    root.title("Fun With Cats")
    Quiz(root)
    root.update()
    root.mainloop()