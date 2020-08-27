from tkinter import *
from tkinter import messagebox
from db import auth_user
from tkinter import ttk
from api import get_upcoming_movies
from systemFeatures.AddNewProjection import AddNewProjection 
from systemFeatures.AddNewEmployee import AddNewEmployee
from systemFeatures.AddNewMovies import AddNewMovie
from systemFeatures.ImageHandling import DisplayPoster
from systemFeatures.ManageScreens import ManageScreen
from systemFeatures.SearchMovie import searchMovie as SearchMovie
from systemFeatures.showtimes import TodaysShowtimes

class AdminDashboard(Tk):
    def __init__(self,userdetails={}):
        Tk.__init__(self)
        self.userdetails = userdetails
        self.onCreate()

     
    def onCreate(self):

        self.geometry('1600x900')
        self['bg'] = 'black'
        # frames starts
        
        frame = Frame(self, bg = 'black') 
        frame.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.98)

        frame_for_buttons = Frame(self ,bg ="dark goldenrod") 
        frame_for_buttons.place(relx = 0.8 ,rely = 0.10, relwidth=0.15 ,relheight=0.60)


        # Title starts 
        greet = Label(frame,text=f"Welcome {self.userdetails['username']} , Admin Dashboard",font = ("Times New Roman",25))
        greet.pack(pady = 7)
        # title ends

        
        #right side button starts
        add_new_employee = Button(frame_for_buttons,text ="Add New Employee",command=self.addNewEmployee)
        add_new_movie = Button(frame_for_buttons, text ="Add New Movie",command=self.addNewMovie)
        add_new_projection = Button(frame_for_buttons, text ="Add New projection",command=self.addNewProjection)
        search_movies = Button(frame_for_buttons, text ="Search Movies",command=self.searchMovie)
        manage_auditoriums = Button(frame_for_buttons, text ="Manage screen/auditorium",command=self.manageScreen)
        # right side button ends

        # positioning of buttons starts
        add_new_employee.pack(pady = 20,padx = 20, fill="x")
        add_new_movie.pack(pady = 20,padx = 20, fill="x")
        add_new_projection.pack(pady = 20,padx = 20, fill="x")
        search_movies.pack(pady = 20,padx = 20, fill="x")
        manage_auditoriums.pack(pady = 20,padx = 20, fill="x")
        # positioning of buttons ends


        todayShowtimeFrame = TodaysShowtimes(frame,bg="red")
        todayShowtimeFrame.place(relx=0.01 ,rely=0.50,relwidth=0.70 ,relheight=0.40)
        # Header
        

        header_frame = Canvas(frame)
        header_frame.place(relx=0.01,rely=0.10,relwidth=0.75,relheight=.30)

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
        scrollbar.place(relx=0.01,rely=0.50,relwidth=0.75)
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

    def addNewEmployee(self):
        AddNewEmployee(self.userdetails).start()
        

    def addNewMovie(self):
        AddNewMovie(self.userdetails).start()

    def addNewProjection(self):
        AddNewProjection(self.userdetails).start()

    def searchMovie(self):
        SearchMovie(self.userdetails).start()
        
    def manageScreen(self):
        ManageScreen(self.userdetails).start()
        
    
    # functions ends






        
       
   

       