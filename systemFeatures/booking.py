from tkinter import *
from tkinter import messagebox,ttk

from db import getAuditoriumDetails,getMovieDetails
from systemFeatures.ImageHandling import DisplayPoster
from systemFeatures.ImageHandling import DisplayPosterFromBytes


class  SeatSelection(Tk):
    def __init__(self,projection=None):
        Tk.__init__(self)
        self.projection = projection
        self.onCreate()

    def onCreate(self):
        HEIGHT = 800
        WIDTH  = 800
        canvas = Canvas(master=self, height=HEIGHT,width=WIDTH)
        canvas.pack()

        base_Frame = Frame(canvas,bg="grey")
        base_Frame.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.98)
        Label(master= base_Frame,text=" Seat Seaction").pack(pady=20)

        movie_details = getMovieDetails(self.projection[1])[0]
        auditorium_details = getAuditoriumDetails(self.projection[2])[0]

        DisplayPosterFromBytes(movie=movie_details ,master= base_Frame ).place(relx=0.10 ,rely =0.10)

    
    def start(self):
        self.mainloop()


    def destory(self):
        self.destroy()
