from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
import requests
import numpy as np
from api import searchMovie,getMovieDetails
from io import BytesIO
import db
from db import addScreentoDb,getAllMovie,getAllScreens

class DisplayPoster(Frame):
    def __init__(self,movie=None,height=160,width=90, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.movie = movie
        self.height = height
        self.width = width
        self.imageHeight = height
        self.imageWidth = width
        self.onCreate()
        


    def onCreate(self):
        img = self.get_poster_image(self.imageHeight,self.imageWidth)
        posterImage = Label(self,image=img)
        posterImage.image=img
        posterImage.pack()
        
        movieTitle = self.movie['title']
        posterLabel = Label(self,text=movieTitle,font=("Helvetica", 12))
        posterLabel.pack()

   
    def get_poster_image(self,height,width):
        try:
            poster_path = self.movie['poster_path']
            print(poster_path)
            # url = f'http://image.tmdb.org/t/p/original/{poster_path}'
            url = f'http://image.tmdb.org/t/p/w500/{poster_path}'
            r = requests.get(url, allow_redirects=True)

            if r.status_code == 200:
                image = Image.open(BytesIO(r.content)).resize((width,height), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(image,master=self)
                return img
            else:
                image = Image.open("poster_placeholder_light.png").resize((width,height), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(image,master=self)  
                return img
        except :
            image = Image.open("poster_placeholder_light.png").resize((width,height), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image,master=self)  
            return img

class DisplayPosterFromBytes(Frame):
    def __init__(self,movie=None,height=160,width=90, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.movie = movie
        self.posterBytes = movie[9]
        self.height = height
        self.width = width
        self.imageHeight = height
        self.imageWidth = width
        self.onCreate()
        


    def onCreate(self):
        img = self.get_poster_image(self.imageHeight,self.imageWidth)
        posterImage = Label(self,image=img)
        posterImage.image=img
        posterImage.pack()
        
        movieTitle = self.movie[1]
        posterLabel = Label(self,text=movieTitle,font=("Helvetica", 12))
        posterLabel.pack()

   
    def get_poster_image(self,height,width):
        try:
            if self.posterBytes is not None :
                image = Image.open(BytesIO(self.posterBytes)).resize((width,height), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(image,master=self)
                return img
            else:
                image = Image.open("poster_placeholder_light.png").resize((width,height), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(image,master=self)  
                return img
        except :
            image = Image.open("poster_placeholder_light.png").resize((width,height), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image,master=self)  
            return img