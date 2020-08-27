from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
from datetime import datetime
from db import getProjections,getMovieDetails
import datetime
from systemFeatures.ImageHandling import DisplayPosterFromBytes
from systemFeatures.booking import SeatSelection
class  TodaysShowtimes(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.onCreate()
        


    def onCreate(self):
        base_frame = Canvas(self)
        base_frame.place(relx=0.005,rely=0.01,relwidth=0.98,relheight=0.98)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=base_frame.yview)
        scrollable_frame = ttk.Frame(base_frame)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: base_frame.configure(
                scrollregion=base_frame.bbox("all")
            )
        )

       
        base_frame.create_window((0, 0), window=scrollable_frame, anchor="nw")
        base_frame.configure(xscrollcommand=scrollbar.set)
        scrollbar.place(relx=0.98,rely=0.00,relheight=1)
        
        
        Label(master=scrollable_frame,text=f"Todays Showtiming").grid(row=1,pady=10)

        now = datetime.datetime.now()
        now = datetime.datetime.now()
        timeoffset = datetime.timedelta(minutes=30)
        fetch_time = now - timeoffset
             
        projections = getProjections(fetch_time.strftime('%Y-%m-%d %H:%M:%S'))

        moviesSet = set()
        for projection in projections:
            moviesSet.add(projection[1])

        listOfMoviesDetails =[]
        for movie_id in moviesSet:
            listOfMoviesDetails.extend(getMovieDetails(movie_id)) 

        row = 2
        for movie_details in listOfMoviesDetails:

            DisplayPosterFromBytes(movie=movie_details,master = scrollable_frame).grid(row=row , rowspan= 5 ,pady=10 )
            col = 1
            btnRow = row
            for projection in projections:
                if projection[1] == movie_details[0]:
                    
                    btn = Button (master=scrollable_frame,text= str(projection[3]) ,command= lambda projection=projection : self.onProjectionBtnPressed(projection=projection))
                    btn.grid(row = btnRow,column=col,padx=10,pady=10)

                    if col <10:
                        col = col + 1
                    else :
                        btnRow = btnRow + 1
                        col = 0



            row =row +5

    def onProjectionBtnPressed(self,projection=None):
        SeatSelection(projection=projection).start()
