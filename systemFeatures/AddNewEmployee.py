from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
import requests
import numpy as np
from api import searchMovie,getMovieDetails
from io import BytesIO
import db
from db import addScreentoDb,getAllMovie,getAllScreens,AddNewEmployeeToDB

# jbvasv


class  AddNewEmployee(Tk):
    def __init__(self,userdetails={}):
        Tk.__init__(self)
        self.userdetails = userdetails
        self.onCreate()

    def onCreate(self):

        HEIGHT = 800
        WIDTH  = 800
        canvas = Canvas(self, height=HEIGHT,width=WIDTH)
        canvas.pack()
        frame_text = Frame(canvas,bg ='black') 
        frame_text.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.98)
        # frame.pack()
                
        Label(frame_text,text = 'ADD NEW EMPLOYEE',fg ="goldenrod",bg ="black",font =("Times New Roman", 30)).grid(row = 0 ,column= 1, pady = 20)

        Label(frame_text, text = 'Username :').grid(row = 3, column = 0, pady = 10) 
        self.username = Entry(frame_text,width = "25")
        self.username.grid(row = 3, column =1, pady = 10)


        Label(frame_text, text= 'Password :').grid(row = 4, column =0, pady = 10)
        self.password = Entry(frame_text, width = "25")
        self.password.grid(row=4, column =1, pady =10)


        Label(frame_text, text= 'Email :').grid(row = 5, column =0, pady = 10)
        self.email = Entry(frame_text, width = "25")
        self.email.grid(row=5, column =1, pady =10)

        # Label(frame_text, text= 'Privileges :').grid(row = 6, column =0, pady = 10)
        # self.password = Entry(frame_text, show ='*', width = "25")
        # self.password.grid(row=6, column =1, pady =10)

        button = Button(frame_text ,text = "Ceate Account", fg = "black", bg = "skyblue", bd = 4, width = "15",command = self.onsubmitpress)
        button.grid(row =7, column =1, pady =10)


    def onsubmitpress(self):
        if len(self.username.get()) == 0:
            messagebox.showerror('Incorrect username',"Username can not be empty")
            return
        if len(self.password.get()) == 0:
            messagebox.showerror("Incorrect password","Password can not be empty")    
            return
        if len(self.email.get()) == 0:
            messagebox.showerror("Incorrect password","email can not be empty")    
            return
       
        msg = AddNewEmployeeToDB(self.username.get(),self.password.get(),self.email.get())
        print(msg)

        if msg[0] == 0:
            messagebox.showinfo("Success", msg[1])
            destory()
    
        if msg[0] == 1:
            messagebox.showerror("Error", msg[1])
       
        

    def start(self):
        self.mainloop()


    def destory(self):
        self.destroy()