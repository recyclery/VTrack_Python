import unittest
import tkinter as tk

from VTrack_tkinter import App 
from tkinter import ttk


class TestAppMethods(unittest.TestCase):
    
    # TODO Method isn't testable, but do so for methods that are...
    def test_populate_volunteers(self):
        app = App(tk.Tk)


if __name__ == '__main__':
    unittest.main()

