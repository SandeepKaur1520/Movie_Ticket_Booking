from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
import requests
import numpy as np
from api import searchMovie,getMovieDetails
from io import BytesIO
import db
from db import addScreentoDb,getAllMovie,getAllScreens





class  SearchMovie(Tk):
    def __init__(self,userdetails={}):
        Tk.__init__(self)
        self.userdetails = userdetails
        self.onCreate()

    def onCreate(self):
        
        
        HEIGHT = 800
        WIDTH  = 450
        canvas = Canvas(self, height=HEIGHT,width=WIDTH)
        canvas.pack()
        frame = Frame(canvas,bg="grey")
        frame.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.98)
        Label(frame,text="Search Movie",font=("Helvetica", 12)).pack()

    def start(self):
        self.mainloop()


    def destory(self):
        self.destroy()


