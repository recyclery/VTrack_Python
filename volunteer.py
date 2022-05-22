from tkinter import ttk

class Volunteer():
    def __init__(self, parent_widget, first, last, img):
        self.parent_widget = parent_widget
        self.first = first
        self.last = last
        self.img = img

        self.label = ttk.Label(parent_widget, text=(self.first + ' ' + self.last))



