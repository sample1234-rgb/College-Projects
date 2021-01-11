# Loading Modules/Header files
from tkinter import *
import sqlite3

class Preview:
    '''Class Preview : To show your data before editing.'''
    def __init__(self,frame): # It it the constructor of class(frame is window,self reference is passed automatically)
        self.window = frame # Self is the class reference ~This statement in C/C++/Java
        # Class Variables(lines 10 - 17) to store information
        # self.first_name = StringVar()
        # self.last_name = StringVar()
        # self.Email = StringVar()
        # self.LinkedIn = StringVar()
        # self.cont1 = IntVar()
        # self.cont2 = IntVar()
        # self.Address1 = StringVar()
        # self.Address2 = StringVar()

    def start(self): # defining a function/method with class reference

        frame1 = Frame(self.window,bg="white",width=300,height=200)#frame widget let u put items together as in container,
        # benefit if you want to adjust this is that placement of objects are not required to be change every time on the window
        frame1.place(relx=0.05,rely=0.1)#(x=150,y=30)
        # Version = Label(self.window, font=("Times New Roman", 10, "bold"), text="Version:\nBeta")
        # Version.place(relx=0.05,rely=0.9)

        frame2 = Frame(self.window, bg="white", width=300,height=200)  # frame widget let u put items together as in container,
        # benefit if you want to adjust this is that placement of objects are not required to be change every time on the window
        frame2.place(relx=0.05, rely=0.5)  # (x=150,y=30)

        frame3 = Frame(self.window, bg="white", width=250,height=200)  # frame widget let u put items together as in container,
        # benefit if you want to adjust this is that placement of objects are not required to be change every time on the window
        frame3.place(relx=0.5, rely=0.1)  # (x=150,y=30)

        basics = Label(self.window,font = ("Times New Roman",12,"bold"),bg= "lime",text = "Basic Information:")
        # Label is used to print text in window
        basics.place(relx=0.05,rely=0.12)
        self.fname = Entry(frame1,fg="gray",bd=0,font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2)
        # Entry widget for taking input,fname = First Name
        self.fname.place(relx= 0.12,rely=0.08) # X: along length of screen(200),Y: along width of screen(50)
        # self.first_name.set('First Name:')#default entry
        self.lname = Entry(frame1,fg="gray",bd=0,font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2)
        self.lname.place(relx=0.56,rely=0.08)#x=400,y=50
        # self.last_name.set("Last Name:")

        self.email = Entry(frame1,fg="gray",font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2)
        self.email.place(relx=0.12,rely=0.25)#x=200,y=100
        # self.Email.set("E-mail:")
        self.link = Entry(frame1,fg="gray",font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2)
        self.link.place(relx= 0.56,rely=0.25)#x=400,y=100
        # self.LinkedIn.set("LinkedIn:")

        self.contact1 = Entry(frame1,fg="gray",font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2)
        self.contact1.place(relx=0.12,rely=0.42)#(x= 200,y=150)
        # self.cont1.set("Phone No.1:")
        self.contact2 = Entry(frame1,fg="gray",font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2)
        self.contact2.place(relx=0.56,rely=0.42)#(x= 400,y=150)
        # self.cont2.set("Phone No.2:")

        self.address1 = Entry(frame1,fg="gray",font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,width = 50)
        self.address1.place(relx=0.07,rely=0.6)#(x= 180,y=200)
        # self.Address1.set("Address 1:")
        self.address2 = Entry(frame1,fg="gray",font = ("Times New Roman",12,"bold"),highlightbackground="Blue",highlightthickness=2,width=50)
        self.address2.place(relx=0.07,rely=0.78)#(x= 180,y=250)
        # self.Address2.set("Address 2:")
        # Ignore this doc_string
        '''
        self.c= []
        x=0
        for _ in range(5):
            a = Canvas(self.window,bg = "red",width = 150*2.2,height = 5)
            a.place(relx = 0+x,rely=0.85)
            self.c.append(a)
            x += 0.2
        for i in range(1,5):
            self.c[i].config(bg = "lime")'''
        # Unoptimized Progress Bar:
        w=150*2.2# showing current level status
        c1 = Canvas(self.window,bg = "green",width = w,height = 5)
        c1.place(relx = 0.0,rely =0.85)
        c2 = Canvas(self.window,bg = "green",width = w,height = 5)
        c2.place(relx = 0.20,rely =0.85)
        c3 = Canvas(self.window,bg = "green",width = w,height = 5)
        c3.place(relx = 0.40,rely =0.85)
        c4 = Canvas(self.window,bg = "green",width = w,height = 5)
        c4.place(relx = 0.60,rely =0.85)
        c5 = Canvas(self.window,bg = "green",width = w,height = 5)
        c5.place(relx = 0.80,rely =0.85)

        next =Button(self.window,text="Next =>",font = ("Times New Roman",12,"bold"),bg="#30c2f2",command = self.Next,relief = RIDGE,padx =5)
        next.place(relx= 0.85,rely= 0.90)   #relx,rely: relative positions acc.to the window size (in %)
        # button widget for linking various events
        self.window.mainloop()#required for showing the window
    def Next(self):#method
        try:
            connection = sqlite3.connect('basic.db')
            cur = connection.cursor()
            # cur.execute('''INSERT INTO information VALUES({0},{1},{2},{3},{4},{5},{6},{7})'''.format(self.first_name.get(),self.last_name.get(),self.Email.get(),self.linkedin.get(),self.cont1.get(),self.cont2.get(),self.Address1.get(),self.Address2.get()))
            connection.commit()
            connection.close()
            # q = Qualify.Qualify(self.window)#from module Qualify create object of class Qualify
            # q.start()
        except:
            pass
if __name__ == "__main__":#Python representation of main function
    window = Tk()#Create window
    window.wm_title("ResumeR")#title of window
    app_wt=800
    scn_wd=window.winfo_screenwidth()
    app_ht=int(0.50*scn_wd)
    window.geometry(f'{app_wt}x{app_ht}+{int((scn_wd-app_wt)/2)}+{int((window.winfo_screenheight()-app_ht)/2)}')
    window.wm_minsize(app_wt,app_ht)#(650, 400)#minimum size of window
    preview = Preview(window)#object of class Basics(frame)
    preview.start()