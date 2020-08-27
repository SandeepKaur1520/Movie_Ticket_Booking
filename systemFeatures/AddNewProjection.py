from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
import requests
import numpy as np
from api import searchMovie,getMovieDetails
from io import BytesIO
import db
from db import addScreentoDb,getAllMovie,getAllScreens,AddNewProjectionToDB
from tkcalendar import Calendar, DateEntry
import datetime



class  AddNewProjection(Tk):
    
    def __init__(self,userdetails={}):
        Tk.__init__(self)
        
        self.userdetails = userdetails
        
        self.listOfMovies  = getAllMovie()  
        self.listOfMoviesNames  = []

        self.listOfAuditorium = getAllScreens()
        self.listOfAuditoriumIDS = []

        self.selectedStartDate = str(datetime.datetime.today().date())

        

        if self.listOfMovies == None:
            messagebox.showerror('Error',"No Moive Exits ,Please add movie before adding projection")
            self.destroy()  
            
        elif self.listOfAuditorium == None:
            messagebox.showerror('Error',"No Auditorium Exits ,Please add Auditorium before adding projection")
            self.destroy()      
        else:
            for row in self.listOfMovies:
                self.listOfMoviesNames.append(row[1])
        
            for row in self.listOfAuditorium:
                self.listOfAuditoriumIDS.append(row[0])
            self.onCreate()

    def onCreate(self):
        HEIGHT = 800
        WIDTH  = 800
        canvas = Canvas(self, height=HEIGHT,width=WIDTH)
        canvas.pack()
        frame = Frame(canvas,bg="grey")
        frame.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.98)
        
        Label(frame,text="Add New Projection",font=("Helvetica", 12)).grid(row=0,columnspan=2,pady=15,padx=15)

        Label(frame,text="Select Movie: ").grid(row=1,pady=10)
        Label(frame,text="Select Auditorium/Screen: ").grid(row=2,pady=10)
        Label(frame,text="Select Date : ").grid(row=3,pady=10)
        Label(frame,text="Select Start Time: ").grid(row=4,pady=10)
        Label(frame,text="Select End Time: ").grid(row=5,pady=10)

        self.moviesChkbox = ttk.Combobox(master=frame)
        self.moviesChkbox['values'] = self.listOfMoviesNames
        self.moviesChkbox.grid(row=1,column=1,pady=10)

        self.auditoriumChkbox = ttk.Combobox(master=frame)
        self.auditoriumChkbox['values'] = self.listOfAuditoriumIDS
        self.auditoriumChkbox.grid(row=2,column=1,pady=10)

        self.date_picker = Calendar(master=frame,date_pattern ='y-mm-dd',mindate = datetime.datetime.today())
        self.date_picker.bind(
            '<<CalendarSelected>>',self.setStartDate
        )
        self.date_picker.grid(row=3,column=1,pady=10)
       
       
        self.startVariable =StringVar(master=frame,value="HH:MM:SS")
        self.endVariable =StringVar(master=frame,value="HH:MM:SS")

        self.startTime_entry  = Entry(master=frame,textvariable=self.startVariable)
        self.endTime_entry = Entry(master=frame,textvariable=self.endVariable)


        self.startTime_entry.grid(row=4,column=1,pady=10)
        self.endTime_entry.grid(row=5,column=1,pady=10)

        Label(frame,text="24Hrs Format (%H:%M:%S) eg (16:30:00)").grid(row=4,column=2,pady=10)
        Label(frame,text="24Hrs Format (%H:%M:%S) eg(12:00:00)").grid(row=5,column=2,pady=10)
        

        submit_btn = Button(master=frame ,text=" Submit ",command=self.onSubmitPressed)
        submit_btn.grid(row=6,column=0,columnspan=3,pady=10)





    def onSubmitPressed(self):
        if self.selectedStartDate == None or self.startVariable.get() == "HH:MM:SS" or self.endVariable.get() == "HH:MM:SS":
            messagebox.showerror("Invalid Input","All fields are mandatory plaese fill them correctly")
        
        else:
            startdatetime_str = str(self.selectedStartDate) + " "  +str(self.startVariable.get())
            enddatetime_str = str(self.selectedStartDate) + " "  +str(self.endVariable.get())

            try:
                startdatetime = datetime.datetime.strptime(startdatetime_str,"%Y-%m-%d %H:%M:%S")
                enddatetime = datetime.datetime.strptime(enddatetime_str,"%Y-%m-%d %H:%M:%S")
            except:
                messagebox.showerror("Invalid Time Input","PLease enter times carefully")   
                return
            movieID = self.listOfMovies[self.moviesChkbox.current()][0]
            auditorium_ID = self.listOfAuditoriumIDS[self.auditoriumChkbox.current()]
            available_seats =  self.listOfAuditorium[self.auditoriumChkbox.current()][1]
            
            msg = AddNewProjectionToDB(movie_ID=movieID,auditorium_ID=auditorium_ID,startTime=startdatetime,endTime=enddatetime,available_seats=available_seats,total_seats=available_seats)
            if msg[0] == 0:
                messagebox.showinfo("Success", msg[1])
                self.destory()

    
            if msg[0] == 1:
                messagebox.showerror("Error", msg[1])
                


    def setStartDate(self,*args):
        self.selectedStartDate = self.date_picker.get_date()
        print(self.selectedStartDate)

    def start(self):
        self.mainloop()


    def destory(self):
        self.destroy()
