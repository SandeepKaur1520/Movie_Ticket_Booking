import tkinter
from tkinter import *
from tkinter import messagebox
from db import auth_user

class Login_page(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.OnCreate()

    
    def OnCreate(self):
        # self =Tk()
        self.geometry('500x500')
        self['bg'] = 'black'


        frame = Frame(self,bg ='black') 
        frame.place(relx = 0.45 ,rely = 0.45, anchor = CENTER)
        # frame.pack()


                
        Label(frame,text = 'Movie Ticket Booking',fg ="dark goldenrod",bg ="black",font =("Times New Roman", 30)).grid(row = 0 ,column= 1, pady = 20)
        Label(frame,text = 'Admin Login',fg ="dark goldenrod",bg ="black",font =("Times New Roman", 20)).grid(row = 2 ,column= 1, pady = 20)




        Label(frame, text = 'Admin ID').grid(row = 3, column = 0, pady = 10) 


        self.username = Entry(frame,width = "25")
        self.username.grid(row = 3, column =1, pady = 10)

        Label(frame, text= 'Password').grid(row = 4, column =0, pady = 10)


        self.password = Entry(frame, show ='*', width = "25")
        self.password.grid(row=4, column =1, pady =10)


        button = Button(frame ,text = "Login", fg = "black", bg = "dark goldenrod", bd = 4, width = "15",command = self.onsubmitpress)
        button.grid(row =5, column =1, pady =10)

                
    def onsubmitpress(self):
        if len(self.username.get()) == 0:
            messagebox.showerror('Incorrect username',"Username can not be empty")
            return
        if len(self.password.get()) == 0:
            messagebox.showerror("Incorrect password","Password can not be empty")    
            return
       
        userdetails = auth_user(self.username.get(),self.password.get())
        print(userdetails)

        if userdetails is None:
            messagebox.showerror("login failed" ,"Username and Password doesn't match")
        else:
            print(userdetails[1])
            if userdetails[1]['privilege'] == 'admin':
                self.destroy()
                from admin_dashboard import AdminDashboard
                adminscreen = AdminDashboard(userdetails = userdetails[1])
                adminscreen.mainloop()
                # admin_dashboard starts
            
            elif userdetails[1]['privilege']== 'employee':
                self.destroy()
                from employee_dashboard import EmployeeDashboard
                employeescreen = EmployeeDashboard(userdetails = userdetails[1])
                employeescreen.mainloop()

    
               

    def start(self):
        self.mainloop()


Login_page().mainloop()      



# image1= tk.PhotoImage(file"{put in the path of the image here**}")
# label_for_image= Label(w, image=image1)
# label_for_image.pack()
