from tkinter import *
from tkinter import messagebox
from db import auth_user
from tkinter import ttk
from api import *
# from systemFeatures.AddNewProjection import 
from systemFeatures.ImageHandling import DisplayPoster
from systemFeatures.showtimes import TodaysShowtimes

class EmployeeDashboard(Tk):
    def __init__(self,userdetails={}):
        Tk.__init__(self)
        self.userdetails = userdetails
        self.onCreate()

     
    def onCreate(self):

        self.geometry('1600x900')

        # frames starts
        
        frame = Frame(self) 
        frame.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.98)

        frame_for_buttons = Frame(self ,bg ="green") 
        frame_for_buttons.place(relx = 0.75 ,rely = 0.10, relwidth=0.20 ,relheight=0.30)


        # Title starts 
        greet = Label(frame,text=f"Welcome {self.userdetails['username']} , Employee Dashboard",font = ("Times New Roman",25))
        greet.pack(pady = 7)
        # title ends

        
        #right side button starts
        new_booking_btn = Button(frame_for_buttons, text ="New Booking",command=self.manageScreen)
        # right side button ends

        # positioning of buttons starts
        new_booking_btn.pack(pady = 20)
        # positioning of buttons ends

        todayShowtimeFrame = TodaysShowtimes(frame,bg="red")
        todayShowtimeFrame.place(relx=0.01 ,rely=0.50,relwidth=0.70 ,relheight=0.40)

        # Header
        

        header_frame = Canvas(frame)
        header_frame.place(relx=0.01,rely=0.10,relwidth=0.70,relheight=.30)

        scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=header_frame.xview)
        scrollable_frame = ttk.Frame(header_frame)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: header_frame.configure(
                scrollregion=header_frame.bbox("all")
            )
        )



        upcoming_movie = get_upcoming_movies(region='in')
        header_frame.create_window((0, 0), window=scrollable_frame, anchor="nw")
        header_frame.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(relx=0.01,rely=0.42,relwidth=0.80)
        Label(scrollable_frame,text="Upcoming Movies",font=("Helvetica", 15)).grid(row=0,columnspan=5,stick=W)
       

      
        i = 0
        if upcoming_movie:
            for movie in upcoming_movie: 
                print(movie['title'])
                frmae = DisplayPoster(master=scrollable_frame,movie=movie,height=160,width=90)
                frmae.grid(row= 1,column=i,pady=10,padx=10)
                i += 1

        

    def start(self):
        self.mainloop()


    def destory(self):
        self.destroy()



    # functions for right side buttons
        
    def manageScreen(self):
        pass
        
    
    # functions ends






        
       
   

       