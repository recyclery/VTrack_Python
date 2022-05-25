'''
VTrack_tkinter.py

Basic tkinter-based python script that allows volunteers to log in and
to register new volunteers. This should also easily export summaries of
volunteer hours and potentially send a monthly summary of the hours
to the volunteer coordinator.
'''

import numpy as np
import pandas as pd
import sqlite3
import tkinter as tk

from tkinter import ttk
from sqlalchemy import create_engine
from PIL import ImageTk
from volunteer import Volunteer
from datetime import datetime

# main application definition
# todo: - add additional widgets (sign in widget, create user widget etc)
#       - read from sqlite database (see below for some basic SQL queries)
class App(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.width = tk.Tk.winfo_screenwidth(self)
        self.height = tk.Tk.winfo_screenheight(self)

        self.geometry(str(self.width) + 'x' + str(self.height))
        self.title('VTrack')
        self.resizable(0, 0)

        # grid column config
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(2, weight=1)

        self.createWidgets()

    def createWidgets(self):
        # Generates the user I/O
        self.user_io_frame = ttk.Frame(self)
        self.user_io_frame.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.generate_user_io_frame(self.user_io_frame)

        # Populates a list of currently signed in volunteers
        # TODO integrate this in w/ a sign in feature
        self.volunteer_frame = ttk.Frame(self)
        self.volunteer_frame.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        self.populate_volunteers_frame(self.volunteer_frame)
    
    def generate_user_io_frame(self, parent_frame):
        register_button = ttk.Button(parent_frame, text='Register', default='active', command=None)
        register_button.grid(column=0, row=0, sticky=(tk.W, tk.N, tk.E, tk.S), padx=5, pady=5)
        
        sign_in_button = ttk.Button(parent_frame, text='Sign In', default='active', command=None)
        sign_in_button.grid(column=0, row=1, sticky=(tk.W, tk.N, tk.E, tk.S), padx=5, pady=5)
        
        with ImageTk.Image.open('./logos/TWFT-logo-fb-01.png').resize([400,400]) as im:
            logo = ImageTk.PhotoImage(im)
        
        img_label = ttk.Label(parent_frame, image=logo)
        img_label.image = logo
        img_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

    def populate_volunteers_frame(self, parent_frame):
        # Temporary - replace with sqlite querying 
        temp_volunteer_list = ['Nathan Mack', 'Joe Bob', 'Bob Joe', 'Jill Franks', 'Rusty Fender', 'Broken Derailleur']
        
        for idx, volunteer in enumerate(temp_volunteer_list):
            name = volunteer.split()
            volunteer_label = Volunteer(parent_frame, name[0], name[1], None).label
            volunteer_label.grid(column=0, row=idx, sticky=tk.W, padx=5, pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()

### helpful sqlite commands ###
# 
# ** list all tables **
# SELECT name FROM sqlite_master WHERE type='table';
# 
# 
# ** list columns in table **
# PRAGMA table_xinfo([table name])

### load the data into the system ###
# conn = sqlite3.connect('./Volunteers.sqlite3')
# cur = conn.cursor()

# table_list_query = """ SELECT name
#                         FROM sqlite_master
#                         WHERE type='table' """
# cur.execute(table_list_query)
# print(f"{cur.fetchall()}")

### exploring the shape of the tables ###
# workers_sql = """PRAGMA table_xinfo(events)"""
# cur.execute(workers_sql)
# print(cur.fetchall())


### Looking at how to do this with Pandas ###
# conn = create_engine('sqlite://<PATH>')
# sql_query = """ SELECT * FROM workers"""
# workers_df = pd.read_sql_query(sql_query, conn)
# workers_df.info() # and all of that good pandas stuff