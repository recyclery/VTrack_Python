'''
VTrack_tkinter.py

Basic tkinter-based python script that allows volunteers to log in and
to register new volunteers. This should also easily export summaries of
volunteer hours and potentially send a monthly summary of the hours
to the volunteer coordinator.



'''

# import what we need
import numpy as np
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import tkinter as tk
from PIL import ImageTk
# from tkinter import ttk

from datetime import datetime



# start up the tkinter 
b_tk = tk.Tk


# main application definition
# todo: - add additional widgets (sign in widget, create user widget etc)
#       - read from sqlite database (see below for some basic SQL queries)
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(padx= 10, pady = 10)
        self.createWidgets()

    def createWidgets(self):
        # banner
        self.banner = tk.Canvas(master=self)
        self.banner.pack(expand=tk.YES)
        with ImageTk.Image.open('./logos/TWFT-logo-fb-01.png').resize([200,200]) as im:
            logo = ImageTk.PhotoImage(im)
        self.logo = logo
        self.banner.create_image(0, 0, anchor=tk.NW, image=self.logo)
        self.banner.grid(padx=10, pady = 10, column=0, row= 0)

        # 

# instantiation
app = Application()
app.master.title('Sample Application')
app.mainloop()

datetime.now()



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